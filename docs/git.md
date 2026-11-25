# Git 초보 가이드
Git은 파일 변경 이력을 저장하는 도구이고 GitHub는 원격 저장소 서비스입니다. 데이터 자체가 아니라 코드와 문서를 관리합니다.
스타터는 가이드 배포용으로 유지하고 실제 분석 프로젝트는 별도 로컬 Git 저장소로 관리하세요. 원격 저장소가 없는 로컬 Git도 가능합니다.
작업 전 git status, 변경 후 git diff를 확인합니다. 민감 데이터가 포함되지 않은 파일만 명시적으로 git add 파일명으로 추가하고 git diff --cached로 확인합니다. git commit -m "분석 코드 수정"으로 기록합니다. git add . 및 자동 push는 피하세요.
이력 확인: git log --oneline. 이미 공유한 커밋의 취소는 git revert를 검토합니다. 강제 push, reset --hard, clean -fd는 초보자가 자동 실행하지 않도록 합니다.
스타터 업데이트는 깨끗한 작업 공간에서 git pull --ff-only로 받고 실제 분석 프로젝트에는 필요한 변경만 검토 후 반영하세요.
