SHS Demo App + Git Collaboration Lab

간단한 Python HTTP 서버(로컬 `shs` 모듈)와 데모 애플리케이션(`app.py`)을 포함한 리포지토리입니다. 라우팅, 정적 파일 서빙, 텍스트/JSON 응답을 제공하며, 이 코드베이스를 활용해 Git 협업 실습 자료도 함께 제공합니다.

## 빠른 시작
- 요구 사항: Python 3.9+ (외부 패키지 없음)
- 실행: `python app.py`
- 접속: 브라우저에서 `http://127.0.0.1:8080/`

## 기본 엔드포인트
- `GET /` 또는 `/index.html`: `public/index.html` 정적 파일 반환
- `GET /hello/{name}`: 텍스트 응답 예제
- `GET /echo`: 요청 메타데이터를 JSON으로 에코
- `GET /add/{a}/{b}`: 간단 계산(덧셈) 결과 반환

예시 curl:
- `curl http://127.0.0.1:8080/hello/world`
- `curl http://127.0.0.1:8080/echo`
- `curl http://127.0.0.1:8080/add/1/2`

## 프로젝트 구조
- `app.py`: 애플리케이션 엔트리포인트. 라우트 등록과 정적 파일 서빙 제어
- `calculator.py`: 데모 계산 로직(실습에서 확장/충돌 유도 지점 포함)
- `public/`: 정적 자원(예: `index.html`)
- `shs/`: 최소 HTTP 서버/라우터/요청/응답 유틸 모듈
- `exercises/`: Git 협업 실습 문서
  - `git-collab-lab/README.md`: 실습 개요
  - `tasks/00-solo-mode.md`: 혼자서 A/B 역할 시뮬레이션 가이드
  - `tasks/01-branch-merge.md`: 브랜치/충돌/머지 실습
  - `tasks/02-pr-rebase.md`: PR 리뷰 + rebase 실습
- `.github/pull_request_template.md`: PR 템플릿
- `.gitignore`: Python 프로젝트용 기본 규칙

## 개발 가이드(간단)
- 라우트 추가: `app.py`에서 `router.add("METHOD", "/path/{params}", handler)` 형식으로 등록
- 핸들러 시그니처: `def handler(req: Request, params: Dict[str, str]) -> Response`
- 응답 도우미: `shs.response.text(...)`, `shs.response.json(...)`
- 정적 파일: `/` 또는 `/static/...` 경로는 `public/`에서 서비스

## Git 협업 실습
- 실습 개요와 단계는 `exercises/git-collab-lab/README.md`를 참고하세요.
- 혼자 진행 시 `exercises/tasks/00-solo-mode.md`로 A/B 역할을 로컬에서 시뮬레이션할 수 있습니다.

## 참고
- 이 리포는 교육/실습 목적의 최소 예제입니다. 프로덕션 보안/에러 처리/로깅은 단순화되어 있습니다.
