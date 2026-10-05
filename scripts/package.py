"""Build deterministic individual and collection ZIPs from validated sources."""

import hashlib
from pathlib import Path
import zipfile

from validate import ROOT, validate


def build(root=ROOT, output=None):
    problems = validate(root)
    if problems:
        raise ValueError("\n".join(problems))
    output = Path(output) if output else root / "dist"
    output.mkdir(parents=True, exist_ok=True)
    skills = sorted((root / "skills").iterdir())
    groups = [(skill.name, [skill]) for skill in skills] + [("designer-skills", skills)]
    archives = []
    for name, folders in groups:
        archive = output / f"{name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for folder in folders:
                for file in sorted(folder.rglob("*")):
                    if not file.is_file():
                        continue
                    relative = file.relative_to(root / "skills").as_posix()
                    info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
                    info.create_system = 3
                    mode = 0o755 if file.stat().st_mode & 0o111 else 0o644
                    info.external_attr = (0o100000 | mode) << 16
                    info.compress_type = zipfile.ZIP_DEFLATED
                    bundle.writestr(info, file.read_bytes())
        archives.append(archive)
    (output / "SHA256SUMS").write_text("".join(
        f"{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.name}\n"
        for file in archives
    ))
    return archives


if __name__ == "__main__":
    for archive in build():
        print(archive.name)
