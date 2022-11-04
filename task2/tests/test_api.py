import os
import sys

import pytest
from unittest.mock import mock_open, patch
from aiohttp import web

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from routes.file_route import Handler


@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = web.Application()
    handler = Handler()
    app.add_routes(
        [web.get("/file", handler.download), web.post("/file", handler.upload)]
    )
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_upload(cli):
    with patch("builtins.open"):
        resp = await cli.post("/file", data="TEST DATA")
        assert resp.status == 201
        assert await resp.text() == "Done"


@pytest.mark.asyncio
async def test_no_file(cli):
    resp = await cli.get("/file")
    assert resp.status == 404


@pytest.mark.asyncio
async def test_download(cli):
    with (
        patch("os.path.isfile", lambda path: True),
        patch("builtins.open", mock_open(read_data="TEST DATA")),
    ):
        resp = await cli.get("/file")
        text = await resp.text()
        assert text == "TEST DATA"
        assert resp.status == 200
