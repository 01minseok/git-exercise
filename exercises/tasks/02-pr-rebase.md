# Part 2: PR 리뷰 + Rebase로 히스토리 정리

## 목표
- PR 리뷰 코멘트 반영을 작은 fix 커밋으로 쪼갠 뒤, 머지 전에 `rebase -i --autosquash`로 커밋을 정리합니다.

## 단계
1. 정책(권장)
   - “Merge main into feature” 금지
   - “Require linear history” 활성화(가능한 경우)

2. 작은 fix 작업 만들기
   - A/B는 각각 2개 내외의 작은 수정 수행(로그 문구/메시지 포맷/예외 메시지 등)
   - 대상 커밋을 찾고 `git commit --fixup <commit_sha>` 사용

3. 인터랙티브 rebase로 정리
   - `git fetch origin`
   - `git rebase -i --autosquash origin/main`
   - fixup 커밋이 자동으로 원 커밋 뒤에 붙고 squash됨을 확인

4. 푸시 및 PR 업데이트
   - `git push --force-with-lease`
   - PR에서 커밋 로그가 깔끔해졌는지 확인
   - “Rebase and merge” 또는 “Squash merge”로 병합

## 보너스
- `git rebase -i`에서 커밋 순서 재배치, 메시지 표준화(Conventional Commits)
- 같은 충돌 반복 시 `git config rerere.enabled true`로 자동 해결 활용
- `git bisect`로 문제 커밋 탐색 체험

## Solo 모드 팁
- A/B 각각의 디렉터리에서 리뷰 코멘트를 스스로 남기고 `git commit --fixup <sha>`로 반영 후, 병합 직전에 `git rebase -i --autosquash origin/main`로 정리합니다.
- 실제 PR UI가 없다면, 메인 디렉터리에서 머지 전략을 바꿔가며 로그 변화를 비교하세요(`git log --oneline --graph`).
