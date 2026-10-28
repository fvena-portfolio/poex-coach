#!/usr/bin/env python3
"""Inspect a registered worktree without repairing it or changing task state."""

import argparse
import json
import os
from pathlib import Path
import subprocess


def inspect(args):
    path = Path(args.path).resolve(strict=True)
    common = Path(args.common_dir).resolve(strict=True)
    # An inherited Git context must not redirect a command away from this worktree.
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env["GIT_OPTIONAL_LOCKS"] = "0"

    def git(*parts, optional=False):
        result = subprocess.run(
            ["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(path), *parts],
            env=env, capture_output=True, text=True, errors="surrogateescape", check=False,
        )
        if result.returncode and not optional:
            raise ValueError(f"Git inspection failed: {' '.join(parts)}")
        return result.stdout.rstrip("\n") if result.returncode == 0 else None

    top = Path(git("rev-parse", "--show-toplevel")).resolve(strict=True)
    actual_common = Path(git("rev-parse", "--path-format=absolute", "--git-common-dir")).resolve(strict=True)
    problems = []
    if top != path:
        problems.append("path_is_not_worktree_root")
    if actual_common != common:
        problems.append("different_repository_common_dir")
    if problems:
        return {"identity_ok": False, "problems": problems, "path": str(path), "common_dir": str(actual_common)}

    # -z avoids quoting ambiguities and supports spaces or newlines in paths.
    listing = git("worktree", "list", "--porcelain", "-z")
    registered = any(
        part.startswith("worktree ") and Path(part[len("worktree "):]).resolve() == path
        for part in listing.split("\0")
    )
    if not registered:
        problems.append("worktree_not_registered")
    head = git("rev-parse", "HEAD")
    branch = git("symbolic-ref", "--quiet", "--short", "HEAD", optional=True)
    if args.branch is not None and branch != args.branch:
        problems.append("unexpected_branch")
    if args.pinned_head is not None:
        if branch is not None:
            problems.append("review_requires_detached_head")
        if head != args.pinned_head:
            problems.append("unexpected_review_commit")

    operations = []
    for name in ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "rebase-merge", "rebase-apply", "BISECT_START", "sequencer"):
        location = git("rev-parse", "--path-format=absolute", "--git-path", name)
        if Path(location).exists():
            operations.append(name)
    status = git("status", "--porcelain=v1", "-z", "--untracked-files=all")
    return {
        "identity_ok": not problems,
        "problems": problems,
        "path": str(path),
        "common_dir": str(actual_common),
        "head": head,
        "branch": branch,
        "head_changed": args.last_head is not None and head != args.last_head,
        "dirty": bool(status),
        "status_porcelain_z": status,
        "upstream": git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}", optional=True),
        "operations": operations,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True)
    parser.add_argument("--common-dir", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--branch")
    mode.add_argument("--pinned-head", help="Full commit SHA for a detached review worktree")
    parser.add_argument("--last-head")
    args = parser.parse_args()
    try:
        result = inspect(args)
    except (OSError, ValueError) as error:
        result = {"identity_ok": False, "problems": [str(error)]}
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["identity_ok"] and not result.get("operations") else 1


if __name__ == "__main__":
    raise SystemExit(main())
