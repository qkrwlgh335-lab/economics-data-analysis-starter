# 경제학 전공자를 위한 AI 데이터 분석 스타터

코딩 초보자가 Windows에서 Codex 또는 Claude Code와 Python·DuckDB를 이용해 대용량 Parquet 데이터를 분석하는 출발점입니다. 실제 카드 결제 데이터는 이 저장소에 넣지 않습니다.

## 0. 데이터 보안부터 확인
**로컬에서 코드를 실행하는 것과 AI가 로컬에서 실행되는 것은 다릅니다.** Codex/Claude는 원격 모델에 대화, 코드, 도구 출력 등을 보낼 수 있습니다. 가명처리 카드 데이터도 재식별 위험이 있습니다. 데이터 제공기관의 승인 및 사용 약관 확인 전에는 실제 파일을 AI 작업 공간에 연결하거나 실제 스키마·경로·통계·로그를 AI에 전달하지 마세요. 승인되지 않았다면 AI는 가상 데이터로만 코드를 작성하고 실제 실행은 직접 별도 환경에서 하세요. [보안 가이드](docs/security.md)

## 1. 처음 시작하기 (Windows 10/11)
1. [Codex](https://openai.com/codex/)에서 Windows 지원 앱/환경을 확인해 설치하고 로그인합니다. 또는 [VS Code](https://code.visualstudio.com/)와 공식 Codex 확장을 설치합니다. Claude Code는 선택입니다.
2. [Python](https://www.python.org/downloads/) 3.12 또는 3.13, [Git](https://git-scm.com/download/win)을 설치합니다. 이미 설치되어 있다면 먼저 확인하세요. 기존 Python을 제거하지 마세요.
3. 이 비공개 저장소에 초대받은 계정으로 로그인합니다. Git을 설치했다면 PowerShell에서 아래 명령을 실행합니다. 브라우저 인증이 필요할 수 있습니다.

```powershell
git clone https://github.com/qkrwlgh335-lab/economics-data-analysis-starter.git
cd economics-data-analysis-starter
```

Git이 어렵다면 Code → Download ZIP → 압축 풀기로 시작해도 됩니다(변경 이력 관리 기능은 별도 설정 필요). AI 앱에서 이 폴더를 작업 공간으로 엽니다. 실제 데이터가 있는 다운로드 폴더 전체를 열지 마세요.

## 2. AI에게 첫 요청
아래 문장을 복사해 AI에게 보내세요.

> README.md와 AGENTS.md를 읽어줘. 나는 경제학 전공이고 코딩 초보야. 실제 데이터에는 접근하지 말고, 이 폴더에서 Python과 Git 설치 여부를 확인하고 가상 데이터 분석 환경을 준비해줘. 변경하기 전에 이유와 실행할 작업을 설명하고 내 승인을 받아. 오류가 나면 원인을 확인하고 해결해줘. 한 번에 한 단계씩 알려줘.

직접 실행할 경우 PowerShell에서:
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe examples/demo.py
.\.venv\Scripts\python.exe -m unittest discover -s tests
```
3.13만 있다면 첫 명령의 -3.12를 -3.13으로 바꾸세요. 실행 정책 변경이나 관리자 권한은 필요하지 않습니다. setup.ps1은 선택 사항이며 [환경 가이드](docs/setup.md)를 참고하세요.

## 3. 실제 분석으로 넘어가기
데이터 사용 정책이 허용하는 경우에만 진행합니다. 원본은 레포 밖의 별도 폴더에 보관하세요. Parquet은 엑셀처럼 직접 수정하는 파일이 아니라 열 기반 데이터 파일입니다. 반디집 아이콘은 파일 연결일 수 있습니다.
파일 탐색기에서 보기 → 파일 이름 확장명을 켜고 실제 확장자를 확인하세요. DuckDB는 확장자가 없어도 올바른 Parquet 파일을 읽을 수 있습니다.
실제 데이터는 직접 실행하는 별도 환경에서 아래처럼 점검할 수 있습니다(경로는 직접 입력, 결과를 AI에 붙여넣지 않기).
```powershell
.\.venv\Scripts\python.exe scripts/inspect_parquet.py
```
이 도구는 경로를 물어보고 스키마만 표시합니다. --count 옵션은 행 수 계산을 추가합니다. 원본을 수정하지 않습니다. 승인되지 않은 경우 AI에 이 명령을 실행시키지 마세요.

## 4. 자연어 요청 예시 (가상 데이터 기준)
- 거래금액의 분포와 결측치를 확인하고 분석 계획을 제안해줘.
- 월별 거래 건수와 총액을 집계해줘. 환불·중복 처리 기준도 설명해줘.
- 종속변수와 설명변수의 정의부터 확인하고 OLS를 수행해줘. 이분산성에 강건한 표준오차와 신뢰구간을 제시해줘.
- 결과를 인과관계로 단정하지 말고 가정과 한계를 설명해줘.
- 분석 코드 변경 전후 테스트를 실행하고 Git 변경 사항을 보여줘. 자동 push는 하지 마.

## 5. Git은 코드와 문서만 관리
[Git 초보 가이드](docs/git.md)를 참고하세요. 실제 분석은 스타터와 분리된 로컬 작업 공간에서 수행하고, 코드 변경 이력만 저장하세요. 원본·파생 데이터·노트북 출력·비밀정보는 commit/push하지 않습니다. .gitignore는 보안 장치가 아닙니다.

## 6. AI 작업 방식
AGENTS.md(Codex), CLAUDE.md(Claude Code)와 .agents/skills, .claude/skills에 분석용 지침이 있습니다. Skills는 모델 학습이 아니라 업무 매뉴얼입니다. 자동 적용 여부는 도구 버전 및 설정에 따라 달라지므로 첫 요청에서 직접 읽으라고 지정하세요. 외부 Skills 설치는 필수가 아닙니다. **[Superpowers · Grill Me · Ponytail 설치 및 사용법](docs/skills.md)** 을 참고하세요. 기본 제공 Skills 5종(parquet, econometrics, validation, beginner-workflow, git-safety)은 별도 설치 없이 프로젝트에 포함되어 있습니다.

## 추가 문서
- [환경 설정](docs/setup.md)
- [데이터 보안](docs/security.md)
- [Git](docs/git.md)
- [경제학 분석 절차](docs/analysis.md)
- [Skills 설치 및 실전 사용법](docs/skills.md)

가상 데이터 예제는 학습용입니다. 실제 경제적 결론이나 인과효과를 나타내지 않습니다.
