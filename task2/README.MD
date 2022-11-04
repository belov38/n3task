# Mini Rest API application

API ables to store and retrieve data on the server in a datafile.

Starting API server:
```shell
python -m aiohttp.web -H localhost -P 5000 api:init_func
```

In order to configure chunk size or data file name copy and edit _.env-sample_

## Endpoints:
Get content of datafile or return 404 error:
```
GET http://localhost:5000/file
```

Upload datafile:
```
POST http://localhost:5000/file
```

## Testing
```shell
cd tests
pytest test_api.py
```
