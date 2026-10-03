"""Check distributable archives and failures that could break isolated installs."""

import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package import build
from validate import validate


class PackagesTest(unittest.TestCase):
    def test_archives_contain_complete_independent_skills(self):
        with tempfile.TemporaryDirectory() as folder:
            archives = build(output=folder)
            for archive in archives:
                names = ([archive.stem] if archive.stem != "agent-skills"
                         else sorted(p.name for p in (ROOT / "skills").iterdir()))
                expected = {p.relative_to(ROOT / "skills").as_posix(): p.read_bytes()
                            for name in names for p in (ROOT / "skills" / name).rglob("*")
                            if p.is_file()}
                with zipfile.ZipFile(archive) as bundle:
                    self.assertIsNone(bundle.testzip())
                    self.assertEqual(set(bundle.namelist()), set(expected))
                    for name, content in expected.items():
                        self.assertEqual(bundle.read(name), content)
                for name in names:
                    self.assertIn(f"{name}/SKILL.md", expected)
                    self.assertIn(f"{name}/LICENSE", expected)
            for line in (Path(folder) / "SHA256SUMS").read_text().splitlines():
                digest, name = line.split("  ")
                self.assertEqual(digest, hashlib.sha256((Path(folder) / name).read_bytes()).hexdigest())
            first = {p.name: p.read_bytes() for p in archives}
            self.assertEqual(first, {p.name: p.read_bytes() for p in build(output=folder)})

    def test_missing_reference_and_cross_skill_dependency_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            copy = Path(folder) / "repo"
            shutil.copytree(ROOT / "skills", copy / "skills")
            shutil.copy2(ROOT / "LICENSE", copy / "LICENSE")
            entry = copy / "skills" / "patchwork" / "SKILL.md"
            original = entry.read_text()
            for target in ("missing.md", "../spike/SKILL.md"):
                entry.write_text(original + f"\n[Required resource]({target})\n")
                self.assertTrue(any(target in error for error in validate(copy)))
                with self.assertRaises(ValueError):
                    build(copy, copy / "dist")


if __name__ == "__main__":
    unittest.main()
