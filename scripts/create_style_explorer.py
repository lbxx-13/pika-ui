#!/usr/bin/env python3
"""Copy the Pika UI comparison page and print a URL for local candidates."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
from urllib.parse import urlencode


def parse_candidate(value: str) -> tuple[str, str, str]:
    parts = value.split("|", 2)
    if len(parts) < 2 or not parts[0].strip() or not parts[1].strip():
        raise argparse.ArgumentTypeError(
            "candidate format is NAME|PATH[|NOTE], for example 'Direction A|./a.html|Quiet'"
        )
    return parts[0].strip(), parts[1].strip(), parts[2].strip() if len(parts) == 3 else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="output HTML path; parent directory must exist")
    parser.add_argument("--candidate", action="append", required=True, type=parse_candidate, help="NAME|PATH[|NOTE], repeat up to three times")
    args = parser.parse_args()

    if len(args.candidate) > 3:
        parser.error("provide at most three candidates")
    output = args.output.expanduser().resolve()
    if not output.parent.is_dir():
        parser.error(f"output directory does not exist: {output.parent}")

    skill_root = Path(__file__).resolve().parents[1]
    template = skill_root / "assets" / "style-explorer.html"
    output.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
    logo = skill_root / "assets" / "pika-ui-logo.png"
    shutil.copyfile(logo, output.parent / "pika-ui-logo.png")

    query: list[tuple[str, str]] = []
    for key, (title, source, note) in zip(("a", "b", "c"), args.candidate):
        if "://" in source:
            resolved_source = source
        else:
            candidate_path = Path(source).expanduser().resolve()
            resolved_source = Path(os.path.relpath(candidate_path, output.parent)).as_posix()
        query.extend(((key, resolved_source), (f"{key}-title", title)))
        if note:
            query.append((f"{key}-note", note))

    print(f"Created: {output}")
    print(f"Open: {output.as_uri()}?{urlencode(query)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
