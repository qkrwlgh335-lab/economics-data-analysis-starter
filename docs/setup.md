# 환경 설정
Windows PowerShell에서 README의 명령을 한 줄씩 실행합니다. py --version, git --version으로 먼저 설치 여부를 확인합니다. Python 3.12/3.13 권장(기존 3.15 환경은 제거하지 않음). 패키지 호환 문제를 줄이기 위한 선택입니다.
가상환경은 프로젝트별 패키지 공간입니다. 활성화 없이 .\.venv\Scripts\python.exe를 직접 사용하면 PowerShell 실행 정책 문제를 피할 수 있습니다. setup.ps1은 실행이 허용된 환경에서만 .\setup.ps1로 실행합니다. 정책 우회는 하지 않습니다.
VS Code는 선택: Python, Jupyter, 공식 Codex 또는 Claude Code 확장을 설치하고 인터프리터를 .venv로 지정합니다. 앱과 CLI 지원 여부는 각 공식 문서 확인. 무료 사용량 및 계정별 제한은 달라질 수 있습니다.
DuckDB는 Python 패키지로 설치하므로 duckdb --version 대신 .venv의 Python에서 import duckdb로 확인합니다.
가상 데이터 예제부터 성공한 뒤 실제 환경은 별도 승인 절차를 거칩니다.
