# rnd-eval-skills — 정부 R&D 사업 평가 Agent Skills

정부 R&D 사업(국가연구개발사업)을 **평가하는 쪽**에서 반복되는 분석 단계 여섯 개를 Agent Skill로 쪼갰습니다. 스킬 하나 = `SKILL.md` 하나, 서로 의존하지 않고, 복사만 하면 Claude Code·Codex·Cursor 등 [Agent Skills](https://agentskills.io) 표준을 읽는 에이전트에서 바로 씁니다.

| 스킬 | 입력 | 출력 | 묻는 것 |
|---|---|---|---|
| [`program-logic-check`](program-logic-check/SKILL.md) | 사업설명자료·전략계획서·성과계획서 | 투입–활동–산출–결과 사슬 표 + 끊긴 고리 | 이 사업은 돈이 어떻게 성과가 된다고 말하는가, 어디가 비었는가 |
| [`indicator-audit`](indicator-audit/SKILL.md) | 성과지표 목록(지표명·산식·목표치) | 지표별 판정표(연계성·유형·질적·산식·외부요인·목표치 근거) | 지표가 성과목표를 실제로 재는가 |
| [`budget-trend-read`](budget-trend-read/SKILL.md) | 연도별 예산·집행 표 | 증감 분해표 + 기준 변경 각주 + 집행률/실집행률 구분 | 늘고 줄었다는 숫자가 무엇 때문인가 |
| [`overlap-screen`](overlap-screen/SKILL.md) | 사업 목록(목적·대상·기술분류) | 유사·중복 후보표(3축 겹침·근거·확인할 자료) | 같은 돈이 두 번 나가는가, 연계가 빠졌는가 |
| [`impact-claim-check`](impact-claim-check/SKILL.md) | 성과 서술문·성과 보고 | 주장–근거 대응표(외부 확인 가능/불가·직접 수혜 반영·외부요인) | 성과 문장이 근거 범위를 넘는가 |
| [`eval-report-skeleton`](eval-report-skeleton/SKILL.md) | 위 다섯 결과 | 평가보고서 골격(md) — 판정마다 근거 문장 자리 | 판정이 어느 근거에서 나왔는지 따라갈 수 있는가 |

## 언제 쓰면 좋은가

사업설명자료를 처음 읽을 때는 `program-logic-check`, 성과지표 표가 있으면 `indicator-audit`, 예산표의 증감 설명이 필요하면 `budget-trend-read`부터 시작하세요. 여섯 개를 모두 돌릴 필요는 없습니다. 여러 검토 결과를 모아 보고서 초안을 만들 때 `eval-report-skeleton`으로 넘어갑니다.

강점은 **반복되는 평가 질문·근거 위치·출력 양식을 함께 제공한다**는 점입니다. 담당자가 달라도 같은 항목을 확인하기 쉽고, 자료가 없는 부분을 `[확인 필요]`로 남기도록 합니다. 스킬은 실행 프로그램이나 법령 데이터베이스가 아니라 AI에게 주는 작업 지침입니다. 결과는 사용한 모델·제공 자료에 따라 달라지며 원문 대조가 필요합니다.

## 첫 사용 예시

`indicator-audit`를 설치한 뒤 사업설명자료와 지표표를 함께 제공하고 다음처럼 요청합니다.

> indicator-audit 스킬로 첨부한 사업의 성과지표를 점검해줘.
> 사업유형·성과목표는 사업설명자료의 문장을 사용하고 출처 쪽을 적어줘.
> 지표명·산식·목표치 근거별 판정표를 만들고, 자료가 없는 곳은 확인 필요로 남겨줘.
> 지표를 바꿀 필요가 있더라도 새 목표치 숫자를 임의로 만들지 말아줘.

기대 결과는 **지표별 판정표 + 판단 근거 + 추가로 필요한 자료 목록**입니다. 지표 이름만 주면 목표 연계성이나 산식의 적정성은 판정하지 못할 수 있습니다. [시범 실행](docs/)은 출력 형태를 익히는 용도이며 모든 실제 사업에서 같은 성능을 보장하지 않습니다.

## 다른 묶음과 다른 점

- **근거 절차 절** — 스킬마다 어느 법 조문·어느 지침 어느 절을 따르는지 적었습니다. 법은 2026-10-20 현행 원문(국가법령정보)으로 대조했고, 지침은 읽은 판(과기정통부 「국가연구개발사업 성과목표·지표 설정 안내서」 6차, 국회의정연수원 「예결산검토 표준교재」 3권 2024)의 절·쪽을 적었습니다. 조문·쪽이 없는 주장은 넣지 않았습니다.
- **지어내지 않는 것 절** — 입력에 없는 수치·목표치·법령 조항·사업명은 `[확인 필요]`로 두고 메우지 않습니다. 사업 코드·지표 코드에 이름을 붙이지 않습니다.
- **2026년 제도 변화 반영** — 재정사업 자율평가(부처 자체평가)가 폐지되고 외부 통합 성과평가로 바뀌었습니다(기획예산처 「2026년 재정사업 성과관리 추진계획」, 2026-01-27 국무회의 보고, 보도 기준). 결과 분류(정상 추진·개선 필요·감액·폐지·통합)는 `eval-report-skeleton`이 그대로 씁니다. **세부 평가지표·배점은 공개 원문을 확보하지 못해 적지 않았습니다.**

## 설치

먼저 저장소를 받습니다. 스킬 폴더 단위로 설치하며, 이미 같은 이름이 설치되어 있다면 기존 내용을 먼저 비교하세요.

```bash
git clone https://github.com/parkjui92/rnd-eval-skills.git
```

**Codex 개인용 설치**(현재 터미널 위치에서 실행):

```bash
mkdir -p ~/.agents/skills
cp -R rnd-eval-skills/indicator-audit ~/.agents/skills/
```

프로젝트에서만 쓰려면 대상 프로젝트의 `.agents/skills/indicator-audit/`에 복사합니다. Codex CLI·IDE에서는 `$indicator-audit`로 명시해 부르거나 스킬 선택 목록에서 고릅니다. [공식 설치 위치·호출 안내](https://learn.chatgpt.com/docs/build-skills)를 참고하세요.

**Claude Code 개인용 설치**:

```bash
mkdir -p ~/.claude/skills
cp -R rnd-eval-skills/indicator-audit ~/.claude/skills/
```

프로젝트용은 대상 프로젝트의 `.claude/skills/`에 둡니다. 다른 에이전트는 해당 제품의 스킬 탐색 경로를 확인하세요. 설치 기능이 없는 채팅에서도 `SKILL.md` 본문과 입력 자료를 함께 제공할 수 있지만 자동 선택·파일 접근 방식은 제품마다 다릅니다. 스킬 자체에는 API 키가 없으며, AI 제품 이용 비용과 자료 접근 권한은 별도입니다.

## 점검

```bash
cd rnd-eval-skills
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

## R&D 정책평가 도구 묶음에서의 위치

필요한 단계만 골라 사용할 수 있습니다. 아래 순서는 업무 흐름이며 자동으로 연결된 파이프라인은 아닙니다. 도구 사이에 자료를 옮길 때 식별자·단위·연도·분류를 확인하세요.

| 필요 | 도구 |
|---|---|
| 공식 통계 수집 | [kr-sti-data](https://github.com/parkjui92/kr-sti-data) |
| 과제번호로 논문 추적 | [kr-grant-trace](https://github.com/parkjui92/kr-grant-trace) |
| 기술 분야의 논문·국내 특허 동향 | [sci-concentration](https://github.com/parkjui92/sci-concentration) |
| 논리모형·성과지표 설계 점검 | [rnd-program-logic](https://github.com/parkjui92/rnd-program-logic) |
| 인과효과 추정 전 설계 점검 | [policy-did](https://github.com/parkjui92/policy-did) |
| AI와 평가 문서 검토 | [rnd-eval-skills](https://github.com/parkjui92/rnd-eval-skills) |
| 예산표 금액 대조 | [won-diff](https://github.com/parkjui92/won-diff) |

## 라이선스

MIT. 인용한 법령은 국가법령정보센터, 안내서·교재는 각 발행기관의 저작물이며 여기에는 절·쪽 참조만 두었습니다.
