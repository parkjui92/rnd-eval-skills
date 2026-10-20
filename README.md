# rnd-eval-skills — 정부 R&D 사업 평가 Agent Skills

정부 R&D 사업(국가연구개발사업)을 **평가하는 쪽**에서 반복되는 분석 단계 여섯 개를 Agent Skill로 쪼갰습니다. 스킬 하나 = `SKILL.md` 하나, 서로 의존하지 않고, 복사만 하면 Claude Code·Codex·Cursor 등 [Agent Skills](https://agentskills.io) 표준을 읽는 에이전트에서 바로 씁니다.

| 스킬 | 입력 | 출력 | 묻는 것 |
|---|---|---|---|
| [`program-logic-check`](program-logic-check/SKILL.md) | 사업설명자료·전략계획서·성과계획서 | 투입–활동–산출–결과 사슬 표 + 끊긴 고리 | 이 사업은 돈이 어떻게 성과가 된다고 말하는가, 어디가 비었는가 |
| [`indicator-audit`](indicator-audit/SKILL.md) | 성과지표 목록(지표명·산식·목표치) | 지표별 판정표(연계성·유형·질적·산식·외부요인·목표치 근거) | 지표가 성과목표를 실제로 재는가 |
| [`budget-trend-read`](budget-trend-read/SKILL.md) | 연도별 예산·집행 표 | 증감 분해표 + 기준 변경 각주 + 집행률/실집행률 구분 | 늘고 줄었다는 숫자가 무엇 때문인가 |
| [`overlap-screen`](overlap-screen/SKILL.md) | 사업 목록(목적·대상·기술분류) | 유사·중복 후보표(3축 겹침·근거·확인할 자료) | 같은 돈이 두 번 나가는가, 연계가 빠졋는가 |
| [`impact-claim-check`](impact-claim-check/SKILL.md) | 성과 서술문·성과 보고 | 주장–근거 대응표(외부 확인 가능/불가·직접 수혜 반영·외부요인) | 성과 문장이 근거 범위를 넘는가 |
| [`eval-report-skeleton`](eval-report-skeleton/SKILL.md) | 위 다섯 결과 | 평가보고서 골격(md) — 판정마다 근거 문장 자리 | 판정이 어느 근거에서 나왔는지 따라갈 수 있는가 |

## 다른 묶음과 다른 점

- **근거 절차 절** — 스킬마다 어느 법 조문·어느 지침 어느 절을 따르는지 적었습니다. 법은 2026-10-20 현행 원문(국가법령정보)으로 대조했고, 지침은 읽은 판(과기정통부 「국가연구개발사업 성과목표·지표 설정 안내서」 6차, 국회의정연수원 「예결산검토 표준교재」 3권 2024)의 절·쪽을 적었습니다. 조문·쪽이 없는 주장은 넣지 않았습니다.
- **지어내지 않는 것 절** — 입력에 없는 수치·목표치·법령 조항·사업명은 `[확인 필요]`로 두고 메우지 않습니다. 사업 코드·지표 코드에 이름을 붙이지 않습니다.
- **2026년 제도 변화 반영** — 재정사업 자율평가(부처 자체평가)가 폐지되고 외부 통합 성과평가로 바뀌었습니다(기획예산처 「2026년 재정사업 성과관리 추진계획」, 2026-01-27 국무회의 보고, 보도 기준). 결과 분류(정상 추진·개선 필요·감액·폐지·통합)는 `eval-report-skeleton`이 그대로 씁니다. **세부 평가지표·배점은 공개 원문을 확보하지 못해 적지 않았습니다.**

## 설치

```bash
git clone https://github.com/parkjui92/rnd-eval-skills
cp -r rnd-eval-skills/indicator-audit ~/.claude/skills/      # 개인용
cp -r rnd-eval-skills/indicator-audit .claude/skills/        # 프로젝트용
```

슬래시 명령(`/indicator-audit`)으로 부르거나, "이 성과지표 적절한지 봐줘"처럼 말하면 에이전트가 고릅니다. 어떤 LLM에든 `SKILL.md` 본문을 그대로 붙여 넣어도 됩니다.

## 점검

```bash
python3 tests/check_skills.py     # frontmatter·필수 절(근거 절차·지어내지 않는 것·출력 양식) 검사
```

## 함께 쓰는 도구

- [kr-sti-data](https://github.com/parkjui92/kr-sti-data) — KOSIS·NABOSTATS 예산·집행 시계열(`budget-trend-read` 입력)
- [kr-grant-trace](https://github.com/parkjui92/kr-grant-trace) — 과제번호 → OpenAlex 논문(`impact-claim-check`의 논문 성과 하한)
- [fact-verify](https://github.com/parkjui92/fact-verify) — 출처 원문 대조
- [budget-review](https://github.com/parkjui92/budget-review) — 국회 예결산 검토보고서 팀(착안사항 전체)

## 한계

- 스킬은 **문서를 읽고 판정**합니다. 데이터로 효과를 추정하는 일(인과추론)은 범위 밖입니다
- 통합 성과평가의 세부 지표·배점, KISTEP 특정평가 세부 지침은 공개 원문 미확보 — 확보되면 `references/`에 쪽을 적어 넣습니다
- 시범 실행은 안내서가 스스로 든 '보완이 필요한 사례'와 공개 특정평가 보고서 1건으로만 했습니다(`docs/`). 실제 사업설명자료 1건 완주는 미검증

## 라이선스

MIT. 인용한 법령은 국가법령정보센터, 안내서·교재는 각 발행기관의 저작물이며 여기에는 절·쪽 참조만 두었습니다.
