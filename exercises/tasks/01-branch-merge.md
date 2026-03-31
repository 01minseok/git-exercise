# Part 1: 브랜치/충돌/머지

## 시나리오
- A는 곱셈 기능을 추가하고 `/mul/{a}/{b}` 라우트를 등록합니다.
- B는 나눗셈 기능을 추가하고 `/div/{a}/{b}` 라우트를 등록합니다.
- 두 작업은 `calculator.py`와 `app.py`의 같은/인접 라인을 수정하여 충돌을 유도합니다.

## 단계
1. `main` 최신화
   - `git checkout main`
   - `git pull --rebase origin main`

2. 브랜치 생성 (A)
   - `git checkout -b feat/mul`
   - 편집 파일
     - `calculator.py`의 `calculate(a, b)` 구현을 곱셈으로 바꾸거나, `op` 파라미터를 도입해 곱셈을 기본값으로 처리
     - `app.py`에 `GET /mul/{a}/{b}` 라우트를 `add` 인접 라인에 추가
   - 의미 있는 작은 커밋 2~3개로 나누기
   - `git push -u origin feat/mul`

3. 브랜치 생성 (B)
   - `git checkout -b feat/div`
   - 편집 파일
     - `calculate(a, b)`에 나눗셈 동작을 반영(0 나눗셈 처리 포함). A와 같은 블록을 수정해 충돌 유도
     - `GET /div/{a}/{b}` 라우트를 `add` 인접 라인에 추가
   - 작은 커밋 2~3개로 나누기
   - `git push -u origin feat/div`

4. PR 생성 및 리뷰
   - 각자 PR 생성, 템플릿을 상세히 작성(변경 요약, 테스트 방법, 리스크)
   - 리뷰어는 네이밍/예외 처리/경계값에 대해 코멘트

5. 머지 순서와 rebase
   - `feat/div` PR을 먼저 병합(merge 또는 squash)
   - A는 자신의 브랜치에서 rebase
     - `git fetch origin`
     - `git checkout feat/mul`
     - `git rebase origin/main`
     - 충돌 해결 → `git add -A` → `git rebase --continue`
     - `git push --force-with-lease`
   - `feat/mul` PR을 “Rebase and merge” 또는 “Squash merge”로 병합

## 완료 기준
- 충돌이 발생했고 이를 올바르게 해결
- 브라우저/`curl`로 `/mul` 또는 `/div` 엔드포인트 동작 확인
- PR 설명과 리뷰 코멘트가 반영됨

## Solo 모드 팁
- `exercises/tasks/00-solo-mode.md`에 따라 두 작업 디렉터리(A/B)를 만든 뒤, 위 단계를 각 디렉터리에서 번갈아 수행하세요.
- B의 작업을 먼저 `main`에 머지(로컬에서 수동 머지)한 다음, A 디렉터리에서 `git rebase origin/main`으로 충돌을 해결합니다.
