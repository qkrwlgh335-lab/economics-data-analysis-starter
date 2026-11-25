---
name: parquet
description: Process large local Parquet datasets with bounded DuckDB queries; inspect schema, filter, aggregate, export and verify without mutating source.
---
# parquet

## 시작 조건
Parquet 읽기·정제·집계·파일 변환 요청에 사용. docs/security.md 먼저 확인. 승인 전 가상 데이터만.
## 절차
1. 파일인지 폴더인지, 분석 단위, 필수 열, 기간, 결측/환불/중복 정의, 출력 위치를 확인한다. 모르는 경로는 허용 폴더 내에서만 확인.
2. DuckDB Python import와 버전, 디스크 여유, 메모리 한도를 확인. 실제 파일 구조는 승인 환경에서 사람이 확인.
3. 필요한 열만 읽고 조건을 먼저 적용. 일자 형식과 통화 단위를 확인. pandas로 전체 변환 금지.
4. 집계 전후 행 수, NULL 수, 중복 키 수, 합계 차이를 비교. NULL과 0을 구별. 환불을 임의 삭제하지 않는다.
5. 원본이 아닌 새 파일로 저장. 출력 경로가 원본과 동일하지 않은지 확인. 레포 외부 저장. 예상 디스크 사용량과 비용 설명.
## 가상 예제
```python
import duckdb
with duckdb.connect() as con:
    con.execute("SET memory_limit='512MB'")
    con.execute("CREATE TABLE demo AS SELECT i id, i % 12 + 1 month, i * 10 amount FROM range(1, 25) t(i)")
    print(con.sql("SELECT month, count(*) n, sum(amount) total FROM demo GROUP BY month ORDER BY month").fetchall())
```
24건, 월별 2건, 총액 3000이 기대값이다. 실제 파일용 SQL은 승인 후 별도 작성.
## 실패 대응
Out of memory: 열·기간 축소, 집계 우선, 승인된 임시 디스크 사용. 파일 오류: 확장자·권한·실제 형식 확인. 무조건 패키지 재설치하지 않는다.
## 완료 기준
실행한 쿼리, 적용한 제외 기준, 행 수 및 합계 검증, 출력 위치, 남은 한계를 보고. 실제 데이터나 로그는 외부 전송 금지.
