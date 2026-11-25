---
name: parquet
description: Process large Parquet datasets with DuckDB using bounded local queries.
---
# 대용량 데이터
docs/security.md를 먼저 따른다. 승인 전 가상 데이터만 사용한다. 스키마부터 확인하고 필요한 열·조건·집계를 먼저 적용한다. 전체 데이터를 pandas에 올리지 않는다. 메모리와 임시 디스크 사용량을 검토한다. 원본 읽기 전용, 파생물 별도 저장. 환불/중복/결측 기준을 확인한다.
