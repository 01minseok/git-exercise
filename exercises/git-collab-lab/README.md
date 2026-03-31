# Git 협업 실습: Branch → Conflict → Merge → PR → Rebase

이 리포를 사용해 작은 Python 웹앱을 토대로 Git 협업을 연습합니다. 2명 이상이 함께 진행할 때 가장 효과적입니다.

## 목표
- 브랜치 전략 수립과 이슈 기반 개발
- 충돌 재현 및 해결(hunk 이해, 최소 편집)
- PR 리뷰 흐름과 머지 전략(merge/squash/rebase and merge)
- 리베이스 기반 선형 히스토리 유지, `--force-with-lease` 안전 푸시
- `fixup` + `--autosquash`로 커밋 정리

## 역할
- A, B: 기능 개발자
- R: 리뷰어(2명이면 서로 번갈아 리뷰)

## 실습 구성
1) Part 1: 브랜치/충돌/머지 — calculator 기능 확장과 라우트 추가로 충돌 유도
2) Part 2: PR 리뷰 + rebase — 리뷰 반영, fixup/autosquash, 선형 히스토리 유지

각 파트의 구체적인 단계는 `exercises/tasks/01-branch-merge.md`, `exercises/tasks/02-pr-rebase.md` 를 참고하세요.

혼자 진행한다면 `exercises/tasks/00-solo-mode.md`의 "Solo Mode" 가이드를 먼저 따라 A/B 두 역할을 로컬에서 시뮬레이션하세요.

## 사전 준비
- 원격 저장소(예: GitHub)에 push 가능한 권한
- `main` 브랜치 보호(선택): PR 필수, 최소 1명 리뷰, “Rebase and merge” 또는 “Squash merge” 허용, 선형 히스토리 옵션 설정 권장

## 코드 편집 포인트(충돌 유도)
- `calculator.py`의 `calculate(a, b)` 구현부 — 서로 다른 방향으로 수정하도록 과제 지정
- `app.py`의 라우트 등록 인접 라인 — 각자 새 라우트 추가로 hunk 충돌 유도
- `public/index.html` 텍스트 — 서로 다르게 편집하도록 지시해 텍스트 충돌 보조

## 빠른 확인 방법
- 서버 실행: `python app.py`
- 브라우저: `http://127.0.0.1:8080/`
- 엔드포인트: `/hello/{name}`, `/add/{a}/{b}` (추가 과제에서 `/mul`/`/div`를 구현)

예시 명령:
- `curl http://127.0.0.1:8080/hello/world`
- `curl http://127.0.0.1:8080/add/1/2`
- (실습 후) `curl http://127.0.0.1:8080/mul/3/4`
- (실습 후) `curl http://127.0.0.1:8080/div/8/2`

행운을 빕니다! 충돌은 학습의 친구입니다 🙂
