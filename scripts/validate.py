"""Validate portable skill folders and their local Markdown references."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    skills = sorted((root / "skills").iterdir())
    if not skills:
        return ["No skills found"]
    license_text = (root / "LICENSE").read_text()
    for skill in skills:
        if not skill.is_dir() or skill.is_symlink():
            errors.append(f"Unexpected entry: {skill.name}")
            continue
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        match = re.match(r"\A---\n(.*?)\n---\n", entry.read_text(), re.S)
        try:
            metadata = yaml.safe_load(match[1]) if match else None
        except yaml.YAMLError as error:
            errors.append(f"{skill.name}: invalid YAML: {error}")
            continue
        if not isinstance(metadata, dict):
            errors.append(f"{skill.name}: missing YAML metadata")
            continue
        name = metadata.get("name")
        if (name != skill.name or len(skill.name) > 64
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name)):
            errors.append(f"{skill.name}: name must match the folder in kebab-case")
        description = metadata.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{skill.name}: description must contain 1–1024 characters")
        license_file = skill / "LICENSE"
        if not license_file.is_file() or license_file.read_text() != license_text:
            errors.append(f"{skill.name}: include the collection LICENSE")
        for file in sorted(skill.rglob("*")):
            if file.is_symlink():
                errors.append(f"{file.relative_to(root)}: symlinks are not portable")
                continue
            if file.name.startswith(".") or file.name in {"__pycache__", "node_modules"}:
                errors.append(f"{file.relative_to(root)}: keep generated/hidden files outside skills")
            if not file.is_file() or file.suffix != ".md":
                continue
            # Ignore example code fences; only resolve prose resource links.
            prose = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", file.read_text(), flags=re.M | re.S)
            for link in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", prose):
                parsed = urlsplit(link.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (file.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(skill.resolve()) or not target.exists():
                    errors.append(f"{file.relative_to(root)}: missing/nonportable resource {link}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        raise SystemExit("\n".join(problems))
    print("All skill metadata, licenses, and local resource links are valid.")
