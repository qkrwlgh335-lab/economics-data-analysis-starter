# AI Skills 설치 및 실전 사용법

Skill은 AI에게 특정 작업 절차를 알려주는 업무 매뉴얼이다. SKILL.md 자체가 표준 진입점이며, 짧은 파일만으로도 인식될 수 있지만 실제 유용성은 절차와 검증 기준에 달려 있다. 이 저장소의 분석 Skills는 이미 프로젝트 경로에 들어 있다. 외부 플러그인은 별도 선택 설치다.

## 1. 추천 순서
처음에는 기본 제공 parquet, econometrics, validation을 사용한다. 분석 요구를 정할 때 Grill Me, 불필요한 프로그램을 만들려 할 때 Ponytail, 여러 단계의 분석 프로그램을 개발할 때 Superpowers를 선택한다. 세 도구를 모든 요청에 동시에 적용할 필요는 없다.

## 2. Superpowers — 작업 계획과 검증
원본: https://github.com/obra/superpowers (MIT).
- Codex 앱: 왼쪽 Plugins → Coding → Superpowers → 추가(+) → 안내에 따라 설치. 메뉴가 없으면 앱 버전 및 계정 지원 여부를 확인한다.
- Codex CLI: 대화창에 /plugins → Superpowers 검색 → Install Plugin.
- Claude Code: 대화창에서 아래 명령을 실행한다.
```text
/plugin install superpowers@claude-plugins-official
```
공식 마켓에서 검색되지 않으면 원본 README의 별도 마켓 설치 방법을 사용한다.
사용 예: "Superpowers를 사용해서 월별 집계 프로그램의 구현 계획을 세워줘. 가상 데이터로 실패 테스트와 수정 후 테스트를 실행해줘. 실제 데이터 접근 및 자동 commit/push는 하지 마."
간단한 조회에는 전체 개발 워크플로가 과할 수 있다. 계획·테스트가 필요한 작업에 사용한다.

## 3. Grill Me — 분석 요구사항 정리
원본: https://github.com/mattpocock/skills (MIT).
원본 Skill: https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
현재 upstream은 grilling이라는 공통 Skill도 사용하므로 함께 설치한다.
Node.js와 npm이 필요하다. 공식 https://nodejs.org/ 에서 LTS 설치 여부를 확인한다. PowerShell에서 node --version, npm.cmd --version으로 확인한다. 실행 정책 우회 대신 필요한 경우 npx.cmd를 사용한다.
Codex/Claude 선택 설치: 프로젝트 루트의 터미널에서 아래 upstream 설치 명령을 실행한다.
```powershell
npx.cmd skills@latest add mattpocock/skills
```
선택 화면에서 grill-me, grilling, setup-matt-pocock-skills를 선택하고 사용하는 에이전트 및 프로젝트 범위를 선택한다. 설치 화면의 실제 목록을 확인한다. setup 요청에는 로컬 문서 사용, 외부 이슈 등록 금지라고 답한다. 다른 설치 방식과 중복 설치하지 않는다.
Claude Code는 upstream의 마켓 설치 방식도 제공한다(전체 묶음). 필요한 Skill만 설치하는 위 방식이 이 프로젝트에서는 우선이다.
사용 예: Claude 대화창에서 /grill-me, Codex에서는 Skill 선택 메뉴 또는 $grill-me(지원되는 버전). "카드 사용액과 기온의 관계를 분석하려고 해. 분석 단위와 통제변수부터 질문해줘. 가상 데이터만 사용해."
질문 예: 분석 대상은 개인/지역/가맹점 중 무엇인가? 시간 단위는? 명목 금액인가? 인과 추정인가 단순 연관인가? 

## 4. Ponytail — 간단한 해결책 우선
원본: https://github.com/DietrichGebert/ponytail
설치 전 upstream README, LICENSE, hooks 및 스크립트 검토. Node.js가 PATH에 필요할 수 있다.
Claude Code 대화창에서 각각 별도로 실행:
```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```
Codex CLI가 설치된 경우 PowerShell에서:
```powershell
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```
Codex 대화창 /hooks에서 lifecycle hook 내용을 검토하고 안전한 경우에만 승인한다. 새 스레드/앱 재시작 후 확인한다. CLI가 없는 앱 사용자라면 upstream의 단일 Skill 설치 방법을 선택하거나 설치를 생략한다.
사용 예: "Ponytail을 적용해서 DuckDB SQL 한두 개와 필요한 Python 코드만 사용해 월별 집계를 만들어줘. 웹앱, 서버, 추가 DB는 만들지 마. 보안·데이터 검증은 생략하지 마."
upstream의 /ponytail lite 등 모드 명령은 해당 도구가 지원할 때만 사용한다.

## 5. 이미 들어 있는 분석 Skills
| 이름 | 호출 예 | 결과 |
|---|---|---|
| parquet | 대용량 Parquet Skill로 가상 파일을 월별 집계해줘 | SQL, 전처리 기준, 검증 |
| econometrics | 계량경제학 Skill로 분석 설계부터 OLS까지 해줘 | 모형 선택, 표준오차, 해석 |
| validation | 검증 Skill로 분석 코드를 다시 검사해줘 | 테스트, 근거, 한계 |
| beginner-workflow | 초보자 Skill로 환경 오류 해결해줘 | 단계별 점검 및 복구 |
| git-safety | Git Skill로 코드 변경만 저장할 준비를 해줘 | 변경 목록, 안전한 커밋 계획 |

Codex는 .agents/skills, Claude Code는 .claude/skills를 확인한다. 지원되는 경우 $skill-name 또는 /skill-name 사용. 메뉴에 없으면 "해당 SKILL.md를 읽고 적용해줘"라고 명시한다. 재시작 후 새 대화에서 가상 데이터로 확인한다.

## 6. 실제 사용 순서
1. 승인된 가상 데이터 작업 공간에서 Grill Me로 요구를 확정한다.
2. parquet Skill로 필요한 열/집계를 만든다.
3. econometrics Skill로 모형 및 가정 검토를 진행한다.
4. validation Skill로 결과 및 재현성을 확인한다.
5. git-safety Skill로 코드 변경만 검토한다.
Superpowers는 복잡한 코드 변경에, Ponytail은 과도한 설계를 막는 데 선택 적용한다.

## 7. 안전한 설치 원칙
외부 플러그인은 이 저장소에 복제하지 않으며 사용자 PC에 자동 설치하지 않는다. 위 명령은 upstream 문서 기반이며 현재 PC에서 실행 검증된 것은 아니다. 설치 시점에 upstream 버전, 라이선스, 변경 내역, hooks를 확인한다. @latest는 최신 코드 실행을 의미하므로 조직 승인 및 검토 전 실행하지 않는다. 설치된 버전을 기록한다. 권한 상승·자동 hook 승인·전체 디스크 접근·자동 push는 금지한다. 민감한 실제 데이터가 연결된 환경에서는 외부 플러그인을 시험하지 않는다. AGENTS.md보다 외부 Skill의 편의 기능을 우선하지 않는다. 

## 8. 외부 전문 통계 분석 Skills
[통계·계량경제학 Skills 원본 다운로드 및 설치 가이드](statistics-skills.md)를 참고한다. 자체 제작 지침과 별도로 K-Dense Statistical Analysis, Statsmodels, DuckDB 및 인과추론 특화 도구를 선택할 수 있다.
