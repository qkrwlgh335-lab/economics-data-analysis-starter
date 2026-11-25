---
name: git-safety
description: Review Git changes, create safe local checkpoints and recover code without exposing sensitive data.
---
# git-safety

## 절차
1. 작업 전 git status 및 현재 브랜치 확인. 원본/파생물은 레포 밖에 보관.
2. git diff --stat 및 허용된 코드 diff 확인. 민감 데이터가 있을 수 있는 diff는 사람이 직접 검토.
3. 파일을 명시적으로 선택해 staging 계획을 제시. git add . 금지. git diff --cached 및 git status 확인.
4. 사용자 승인 후 코드/문서만 로컬 commit. 원격 push는 별도 승인. 실제 데이터 저장소는 원격 연결을 기본 요구하지 않는다.
5. 복구는 git log --oneline과 git revert 우선 검토. reset --hard, clean -fd, force push 자동 수행 금지.
## 완료 기준
변경 파일, 테스트 결과, 커밋 메시지, 현재 상태, 원격 전송 여부. .gitignore는 기존 추적 파일이나 강제 추가를 막지 못함.
## 사고 대응
민감 데이터 staging/commit 발견 시 push 중단. 관리자에게 보고하고 승인된 이력 정리 절차 수행. 단순 삭제로 해결됐다고 하지 않는다.
