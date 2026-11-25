---
name: beginner-workflow
description: Guide a non-programmer through Windows Python, DuckDB, paths, and debugging with one step at a time.
---
# beginner-workflow

## 절차
1. 사용자의 목표를 평문으로 확인. 이미 알려진 OS/파일명/경로는 재질문하지 않는다.
2. 승인된 작업 폴더에서 환경을 직접 확인: py --version, git --version, 가상환경 존재, Python import duckdb. 명령 실행 권한이 없으면 정확히 복사할 명령 하나만 준다.
3. 파일 확장자 숨김 문제는 탐색기 보기 또는 허용된 범위의 Get-ChildItem으로 확인. 경로를 추측하지 않는다. 민감 데이터 탐색은 보안 승인 전 금지.
4. PowerShell 인용 문제는 긴 py -c 대신 .py 파일과 인자 사용으로 피한다. 오류 메시지의 원인을 먼저 확인하고 무작정 재설치하지 않는다.
5. 변경 전 이유와 승인 요청. 완료 후 실행 결과 및 다음 한 단계 안내.
## 예시
DuckDB CLI 미인식은 Python 패키지 미설치와 다르다. .venv의 python.exe에서 import duckdb로 점검한다.
## 완료 기준
실제 확인된 사실, 실행한 명령, 성공/실패, 다음 한 가지 작업. 전문 용어는 바로 설명하고 사용자에게 동일 작업을 반복시키지 않는다.
