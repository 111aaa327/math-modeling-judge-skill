#!/usr/bin/env python3
"""Create a deterministic file inventory for a frozen review packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def collect(root: Path) -> list[dict]:
    files = [root] if root.is_file() else sorted(p for p in root.rglob("*") if p.is_file())
    base = root.parent if root.is_file() else root
    return [
        {
            "path": str(path.relative_to(base)).replace("\\", "/"),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="Frozen file or directory to inventory")
    parser.add_argument("--out", type=Path, required=True, help="Output JSON manifest")
    parser.add_argument("--label", default="mathematical-modeling review packet")
    args = parser.parse_args()

    packet = args.packet.resolve()
    if not packet.exists():
        raise SystemExit(f"packet does not exist: {packet}")
    payload = {
        "schema_version": 1,
        "label": args.label,
        # Keep manifests portable and avoid leaking a reviewer's local account
        # or directory structure when the audit package is shared.
        "packet_root": packet.name,
        "files": collect(packet),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(payload['files'])} entries -> {args.out}")


if __name__ == "__main__":
    main()


