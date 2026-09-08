from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_review_manifest.py"


class ReviewManifestTests(unittest.TestCase):
    def run_manifest(self, packet: Path, output: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(packet), "--out", str(output), "--label", "blind-v1"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def test_inventory_is_sorted_hashed_and_portable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            packet = root / "packet"
            (packet / "nested").mkdir(parents=True)
            (packet / "z.txt").write_bytes(b"z")
            (packet / "nested" / "a.txt").write_bytes(b"alpha")
            output = root / "manifest.json"

            process = self.run_manifest(packet, output)
            self.assertEqual(process.returncode, 0, process.stderr)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["packet_root"], "packet")
            self.assertNotIn(str(root), json.dumps(payload, ensure_ascii=False))
            self.assertEqual([item["path"] for item in payload["files"]], ["nested/a.txt", "z.txt"])
            self.assertEqual(
                payload["files"][0]["sha256"],
                hashlib.sha256(b"alpha").hexdigest().upper(),
            )

    def test_same_packet_contents_produce_same_manifest_on_different_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payloads = []
            for side in ("left", "right"):
                packet = root / side / "packet"
                packet.mkdir(parents=True)
                (packet / "paper.txt").write_text("same", encoding="utf-8")
                output = root / side / "manifest.json"
                process = self.run_manifest(packet, output)
                self.assertEqual(process.returncode, 0, process.stderr)
                payloads.append(json.loads(output.read_text(encoding="utf-8")))
            self.assertEqual(payloads[0], payloads[1])

    def test_missing_packet_fails_without_creating_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "manifest.json"
            process = self.run_manifest(root / "missing", output)
            self.assertNotEqual(process.returncode, 0)
            self.assertIn("packet does not exist", process.stderr + process.stdout)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()


