# 외부 통계·계량경제학 Skills 설치 가이드

대상: Python과 DuckDB로 대용량 Parquet를 다루는 경제학 전공 초보자. 실제 연구 모형은 아직 미정이므로 기초 통계와 회귀를 우선하고, 패널·인과추론은 필요할 때 추가한다. 아래 링크는 원본이며 자체 제작 Skill과 구별한다.

## 0. 보안
실제 카드 결제 데이터와 연결되지 않은 가상 데이터 전용 작업 공간에서 설치·검토한다. 외부 Skill은 코드 실행, 네트워크 접근, 파일 탐색을 지시할 수 있다. 원격 AI에 실제 데이터, 경로, 열 이름, 출력, 로그를 보내지 않는다. 승인된 데이터 처리 환경은 docs/security.md 참고. 설치 전 원본의 LICENSE, SKILL.md, scripts, references, 의존성 및 커밋을 확인한다. 승인 없이 자동 설치하지 않는다. 설치 방법은 공개 문서 기반이며 Windows/Codex/Claude에서 직접 실행 검증되지 않았다.

## 1. 우선 추천: K-Dense Statistical Analysis + Statsmodels
- 원본 저장소: https://github.com/K-Dense-AI/scientific-agent-skills
- 통계 분석 원본: https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/statistical-analysis
- 회귀·시계열 원본: https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/statsmodels
- 원본 전체 다운로드: https://github.com/K-Dense-AI/scientific-agent-skills/archive/refs/heads/main.zip
- statistical-analysis: 검정 선택, 가정 확인, 효과크기, 신뢰구간, 결과 보고
- statsmodels: 회귀, 잔차 진단, 시계열 모형 등의 Python 사용 지침

원본 README가 제공하는 설치 방법(프로젝트 폴더의 PowerShell, Node.js 필요):
```powershell
npx.cmd skills add K-Dense-AI/scientific-agent-skills
```
선택 화면에서 statistical-analysis와 statsmodels만 선택하고, 실제 사용하는 에이전트(Codex 또는 Claude Code)와 프로젝트 범위를 선택한다. 전체 설치 불필요. npx 실행 전 설치 도구 및 버전을 검토한다. 또는 아래 수동 설치 방법을 사용한다.
사용 예: "statistical-analysis Skill을 읽고 가상 데이터의 분석 목적에 맞는 검정과 가정을 설명해줘." / "statsmodels Skill을 사용해서 가상 월별 지출 데이터로 OLS를 실행하고 잔차와 신뢰구간을 설명해줘."

## 2. 대용량 데이터: DuckDB Skills
- DuckDB 공식 소개: https://duckdb.org/2026/09/16/duckdb-skills
- 커뮤니티 구현(별도 프로젝트): https://github.com/open-source-on-ai/skill-DuckDB
공식 소개와 커뮤니티 저장소를 동일한 구현으로 가정하지 않는다. 커뮤니티 구현은 query, read-file 등 도구 및 스크립트를 제공한다고 설명한다. 설치 전 원본 README에서 실제 경로와 DuckDB CLI 의존성, 라이선스를 확인한다. 현재 Python duckdb 패키지만 있다면 CLI가 별도로 필요할 수 있다. 파일 탐색, 클라우드 저장소 연결, 세션 로그 검색 기능은 민감 데이터 환경에서 사용하지 않는다. 필요한 로컬 read-file/query만 검토하거나 기본 제공 parquet Skill을 유지한다.
사용 예: "가상 Parquet에서 필요한 열만 읽고 월별로 집계해줘. 전체 pandas 변환이나 외부 연결 없이 검증해줘."

## 3. 선택: Anthropic Statistical Analysis
- 원본: https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/statistical-analysis
- 다운로드: https://github.com/anthropics/knowledge-work-plugins/archive/refs/heads/main.zip
기초 통계, 추세, 이상치, 가설검정에 활용. K-Dense와 기능이 겹치므로 동시에 설치할 필요 없음. 수동 설치 시 data/skills/statistical-analysis 폴더 및 필요한 참조·라이선스를 확인해 복사한다. 이름 충돌에 주의한다.

## 4. 선택: EconAgentSkills (패널 및 경제학 연구)
- 원본: https://github.com/JonasWeinert/EconAgentSkills
- 다운로드: https://github.com/JonasWeinert/EconAgentSkills/archive/refs/heads/main.zip
- Python 패널: https://github.com/JonasWeinert/EconAgentSkills/tree/main/_skills/analysis/python-panel-data
- 데이터 관리: https://github.com/JonasWeinert/EconAgentSkills/tree/main/_skills/data/working-with-data
- CC0 1.0 (원본 표기). 참조 자료와 예제 및 프로젝트 공통 AGENT_POLICY.md를 함께 검토한다.
원본 설치 스크립트 사용 예(가상 데이터 전용 환경에서 검토 후):
```powershell
git clone https://github.com/JonasWeinert/EconAgentSkills.git
cd EconAgentSkills
py scripts/install_skills.py --help
```
원본 README의 --skill python-panel-data 및 --dest 옵션으로 대상 프로젝트의 Skill 폴더 지정. 예를 들어 Claude 프로젝트 경로가 C:\analysis\starter라면 --target claude --skill python-panel-data --dest "C:\analysis\starter\.claude\skills"를 검토한다. Codex 지원 플래그는 --help에서 확인하거나 수동 복사를 사용한다. 다른 연구 방법에 필요한 R/Stata는 현재 설치하지 않는다.
사용 예: "python-panel-data Skill로 가상 지역-월 패널의 고정효과와 군집 표준오차 선택을 검토해줘."

## 5. 선택: Econometrics Skill (인과추론 라이브러리 포함)
- 원본: https://github.com/xiaomihu1992/econometrics-skill
- 다운로드: https://github.com/xiaomihu1992/econometrics-skill/archive/refs/heads/main.zip
- MIT (원본 표기), 17개 추정 함수, 예제, 참고 자료 포함.
원본 전체를 별도 폴더에 clone하고 README 및 LICENSE, lib, requirements.txt 검토. 가상환경에서 requirements 설치 후 examples/ols_example.py를 실행하는 방식이 원본 README에 제시되어 있다.
기존 자체 econometrics Skill과 이름이 겹치므로 동시에 활성화하지 않는다. 이 저장소의 기존 Skill을 삭제하거나 덮어쓰지 말고 별도 검토용 프로젝트에서 원본 전체 폴더를 설치한다. 원본에 IV 표준오차 등 알려진 방법별 한계가 명시되어 있다. 사용 목적이 단순 기술통계/회귀라면 설치하지 않아도 된다. 대용량 원본을 통째로 pandas로 로드하지 말 것.

## 6. 수동 다운로드·설치 (Node 없이)
1. 원본 링크에서 Code → Download ZIP, 또는 위 ZIP 링크 사용. 압축을 별도 검토 폴더에 푼다.
2. 원하는 Skill의 SKILL.md, scripts, references, LICENSE 및 상위 공통 정책을 확인한다. 가능하면 검토한 커밋 SHA와 다운로드 날짜를 기록한다.
3. 해당 Skill 폴더 전체를 작업 프로젝트 아래 .agents/skills/ (Codex) 또는 .claude/skills/ (Claude Code)에 복사한다. 이름이 이미 있으면 중단하고 하나만 선택한다. SKILL.md만 복사하면 상대 경로 참조나 실행 파일이 깨질 수 있다.
4. 에이전트를 재시작하고 새 대화에서 해당 SKILL.md를 읽으라고 요청한다. 설치 경로 지원 여부는 각 도구 버전에 따라 확인한다.
5. 예제와 스크립트를 가상 데이터로 실행하여 성공 여부를 확인한다. 의존성 설치는 가상환경에서 별도 승인. 외부 Skill의 전체 데이터 읽기나 네트워크 접근 지침은 사용하지 않는다.

## 7. 친구가 AI에 그대로 보낼 첫 요청
> README.md, AGENTS.md, docs/security.md, docs/statistics-skills.md를 읽어줘. 나는 경제학 전공이고 코딩 초보야. 실제 데이터는 절대 접근하지 마. K-Dense statistical-analysis와 statsmodels의 원본을 검토하고 설치 계획, 필요한 프로그램, 네트워크 접근 여부, 충돌 가능성을 설명해줘. 내 승인 후 프로젝트 범위에 설치하고, 가상 데이터로 통계 분석과 회귀 예제를 실행해 검증해줘. 실제 설치 여부와 테스트 결과를 알려줘.

## 8. 기본 조합
자체 parquet + K-Dense statistical-analysis + statsmodels부터 시작. 모형이 패널/DiD/IV라면 4 또는 5를 추가 검토한다. 외부 Skills의 품질과 통계적 타당성은 별도 검증이 필요하며, 공개 저장소에 존재한다고 안전하거나 정확한 것이 보장되지는 않는다.
