# Solo Mode: 한 사람이 A/B 역할 시뮬레이션

여러 명 대신 혼자서 A/B 두 명을 시뮬레이션하는 방법입니다. `git worktree`를 사용하면 한 저장소에서 여러 작업 디렉터리를 만들어 동시에 작업할 수 있습니다.

## 옵션 A: worktree로 A/B 디렉터리 만들기(권장)

사전 조건: 현재 리포가 `main` 최신 상태라고 가정합니다.

1) A/B 작업 디렉터리 생성

```bash
# 리포 루트에서 실행
git fetch --all
git worktree add ../shs-A -b feat/mul
git worktree add ../shs-B -b feat/div
```

2) 각 작업 디렉터리에서 사용자 정보 분리(선택)

```bash
cd ../shs-A
git config --worktree user.name "Dev A"
git config --worktree user.email "a@example.com"

cd ../shs-B
git config --worktree user.name "Dev B"
git config --worktree user.email "b@example.com"
```

3) 역할 수행 방법

- A 역할: `../shs-A` 디렉터리에서 `exercises/tasks/01-branch-merge.md`의 A 지시를 따릅니다.
- B 역할: `../shs-B` 디렉터리에서 B 지시를 따릅니다.

4) PR/머지 시뮬레이션

- 실제 PR UI 대신, 메인 작업은 원본 리포 디렉터리(또는 셋 중 하나)에서 수행합니다.
- 순서 예시:
  - B가 먼저 완료했다고 가정 → 원본 리포에서 `main`으로 `feat/div`를 병합(merge 또는 squash)
  - A는 `../shs-A`에서 `git fetch --all && git rebase origin/main`으로 충돌 해결 후 `--force-with-lease`로 업데이트

5) 정리(선택)

```bash
# 리포 루트에서
git worktree remove ../shs-A
git worktree remove ../shs-B
```

## 옵션 B: 로컬 bare 원격 + 두 개의 클론

PR 흐름을 더 가깝게 흉내 내려면 로컬 bare 저장소를 원격처럼 사용해 두 개의 클론을 만듭니다.

```bash
# 상위 디렉터리에서
git init --bare shs-remote.git

# 원본 리포에서
git remote remove origin  # 이미 origin이 있다면 유지하거나 다른 이름으로 두세요
git remote add origin ../shs-remote.git
git push -u origin main

# 두 개의 클론 생성
git clone ../shs-remote.git shs-A && cd shs-A && git checkout -b feat/mul
git clone ../shs-remote.git shs-B && cd shs-B && git checkout -b feat/div

# 사용자 정보 분리(선택)
git config user.name "Dev A"; git config user.email a@example.com  # A 클론에서
git config user.name "Dev B"; git config user.email b@example.com  # B 클론에서
```

이후 A/B는 각자 변경을 커밋하고 `origin`에 푸시합니다. PR은 실제 Git 호스팅이 없으므로 생략하고, 메인 클론에서 머지 순서와 rebase를 수동으로 시뮬레이션합니다.

## Solo 진행 팁

- A와 B 작업을 번갈아 수행하며, 의도적으로 같은 파일/인접 라인을 편집해 충돌을 만드세요(`calculator.py`, `app.py`, `public/index.html`).
- 리뷰 코멘트는 커밋 메시지나 TODO 주석으로 스스로 남긴 뒤, `git commit --fixup <sha>`로 반영하고 `git rebase -i --autosquash`로 정리합니다.
- 병합 전략을 바꿔 보며 로그 차이를 비교해 보세요: merge commit vs squash vs rebase and merge.

