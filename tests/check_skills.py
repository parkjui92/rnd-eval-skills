#!/usr/bin/env python3
"""스킬 묶음 형식 점검 — frontmatter(name·description), 필수 절, 금지 표현.

실행: python3 tests/check_skills.py   (exit 0 = 통과)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = ["## 역할", "## 근거 절차", "## 절차", "## 지어내지 않는 것", "## 출력 양식", "## 자기 점검"]
# 판정 스킬이 처방·단정으로 미끄러지는 신호. 출력 양식 코드블록 밖 본문에서만 본다.
FORBIDDEN_IN_BODY = [r"반드시 삭제", r"과장되었다", r"허위", r"중복이다\.", r"적정하다\."]


def body_without_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check(skill_dir: Path) -> list[str]:
    errs = []
    f = skill_dir / "SKILL.md"
    if not f.exists():
        return [f"{skill_dir.name}: SKILL.md 없음"]
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, flags=re.S)
    if not m:
        return [f"{skill_dir.name}: frontmatter 없음"]
    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, flags=re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, flags=re.M)
    if not name or name.group(1).strip() != skill_dir.name:
        errs.append(f"{skill_dir.name}: name이 폴더명과 다름")
    if not desc or len(desc.group(1)) < 80:
        errs.append(f"{skill_dir.name}: description 80자 미만")
    for s in REQUIRED_SECTIONS:
        if s not in t:
            errs.append(f"{skill_dir.name}: 절 없음 {s}")
    # 근거 절차 표에 조문 또는 쪽/절 참조가 있어야 한다
    sec = t.split("## 근거 절차", 1)[-1].split("## 절차", 1)[0]
    if not re.search(r"제\d+조|p\.\d+|Ⅳ\.\d|§", sec):
        errs.append(f"{skill_dir.name}: 근거 절차에 조문·쪽·절 참조 없음")
    body = body_without_code(t)
    for pat in FORBIDDEN_IN_BODY:
        if re.search(pat, body):
            errs.append(f"{skill_dir.name}: 금지 표현 /{pat}/")
    if "[확인 필요" not in t and "판정 불가" not in t and "빈 자리" not in t:
        errs.append(f"{skill_dir.name}: 모르는 것을 표시하는 장치([확인 필요]/판정 불가/빈 자리) 없음")
    return errs


def main() -> int:
    dirs = sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    if not dirs:
        print("스킬 폴더 없음"); return 1
    errs = []
    for d in dirs:
        errs += check(d)
    for e in errs:
        print("FAIL", e)
    print(f"{len(dirs)} skills, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
