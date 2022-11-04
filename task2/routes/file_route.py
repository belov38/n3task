from aiohttp import web
import os


class Handler:
    def __init__(self, datafile: str = 'datafile.dat', chunk_size: int = 512):
        self._datafile = datafile
        self._chunk_size = chunk_size
        pass

    async def download(self, request):
        if not os.path.isfile(self._datafile):
            return web.Response(text='File not found', status=404)

        with open(self._datafile, 'rb') as f:
            payload = f.read()
        return web.Response(body=payload)

    async def upload(self, request):
        if os.path.isfile(self._datafile):
            os.remove(self._datafile)

        async for data in request.content.iter_chunked(self._chunk_size):
            f = open(self._datafile, 'ab')
            f.write(data)
            f.close()
        return web.Response(text="Done", status=201)
