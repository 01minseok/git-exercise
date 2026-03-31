from __future__ import annotations

import json as _json
import logging
import os
from typing import Dict

from shs.request import Request
from shs.response import Response, json, text
from shs.router import Router
from shs.static import serve_file

from calculator import calculate

router = Router()


def hello(req: Request, params: Dict[str, str]) -> Response:
    name = params.get("name", "world")
    return text(f"hello {name}\n")

def add(req: Request, params: Dict[str, str]) -> Response:
    a = params.get("a")
    b = params.get("b")
    result = calculate(int(a), int(b))
    return text(f"result = {result}\n")

def echo(req: Request, params: Dict[str, str]) -> Response:
    payload = {
        "method": req.method,
        "path": req.path,
        "query": req.query,
        "headers": req.headers,
        "body_len": len(req.body),
    }
    return json(_json.dumps(payload))


"""
Git Lab TODO (충돌 유도 지점)
-----------------------------
- Part 1에서 아래 router.add 인접 라인에 각각 새 라우트를 추가하세요.
- 예시: A → `GET /mul/{a}/{b}`, B → `GET /div/{a}/{b}`
- 가능한 한 `add` 라우트와 가까운 곳(같은 블록)에 배치해 충돌을 유도합니다.
"""

router.add("GET", "/hello/{name}", hello)
router.add("GET", "/echo", echo)
router.add("GET", "/add/{a}/{b}", add)


def app(req: Request) -> Response:
    base = os.path.join(os.path.dirname(__file__), "public")
    if req.path == "/" or req.path == "/index.html":
        return serve_file(req, base, "index.html")
    if req.path.startswith("/static/"):
        sub = req.path[len("/static/"):]
        return serve_file(req, base, sub)
    return router.dispatch(req)


if __name__ == "__main__":
    from shs.server import serve
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    print("Serving on http://127.0.0.1:8080 ...")
    serve("127.0.0.1", 8080, app)
