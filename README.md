## sslyze_api

API Endpoint for [github.com/nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) written in Python/Flask and Celery

### Usage

Install Python v2.7+ and pip before proceeding further

1. Install the dev-requirements.txt using `pip install -r dev-requirements.txt`
2. Change to `sslyze_api` directory
3. Start Celery with `celery -A sslyze_api.celery_app worker -l info`
4. Execute `run.py` file with python


### Features

    [x] User Authenticaton
    [x] Token Based Auth
    [ ] Rate Limiting based on IP
    [ ] Logging requests
    [ ] Caching Response


### Stack
- Python 2
- Flask
- sslyze
- celery
- billiard
- sqlalchemy
- sqlite3
- gunicorn
- Docker
