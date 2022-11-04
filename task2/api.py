import os
from aiohttp import web
from routes.file_route import Handler
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = os.getenv("DATA_FILE") or "datafile.dat"
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE") or 512)


def init_func(argv):
    app = web.Application()
    handler = Handler(datafile=DATA_FILE, chunk_size=CHUNK_SIZE)
    app.add_routes(
        [web.get("/file", handler.download), web.post("/file", handler.upload)]
    )
    return app
