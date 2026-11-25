---
name: validation
description: Audit data transformations and econometric outputs using synthetic tests, evidence, and reproducibility checks.
---
# validation

## 시작 조건
분석 결과 검증, 오류 수정, 코드 리뷰, 실행 성공 확인 요청.
## 절차
1. 분석 요구 및 예상 결과를 먼저 작성한다. docs/security.md 준수.
2. 작은 가상 데이터에 정상 거래, 환불, 중복, NULL, 경계 날짜를 넣어 예상 결과를 사람이 계산한다.
3. 기존 코드를 실행해 기대값과 비교한다. 실패하면 원인을 재현하고 최소 변경 후 다시 실행한다.
4. 행 수/합계/중복/결측/기간이 의도와 일치하는지 점검. 회귀는 표본 제외, 변수 단위, 기준 범주, 표준오차, 신뢰구간, 인과 주장 검토.
5. 변경 전후 diff와 테스트 결과를 확인한다. 실제 민감 데이터 출력은 공유하지 않는다.
## 실행 명령
```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```
## 결과 양식
PASS/FAIL/NOT RUN, 실행 명령, 예상값과 실제값, 오류 원인, 수정 파일, 미검증 사항. 테스트 통과가 통계적 타당성을 보장하지 않음을 설명한다.
## 금지
실행하지 않은 테스트를 PASS로 표시, 테스트를 통과시키려 기대값 임의 변경, 원본 수정, 자동 push.
