## sslyze_api

API Endpoint for [github.com/nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) written in Python/Flask and Celery

### Usage

Install Python v2.7+ and pip before proceeding further

1. Install the dev-requirements.txt using `pip install -r dev-requirements.txt`
2. Change to `sslyze_api` directory
3. Start Celery with `celery -A sslyze_api.celery_app worker -l info`
4. Execute `run.py` file with python

**Default credentials**

    username: admin
    password: password
    token: ae027250efaafacd3087085fb1ee787c
  
  
**Available API routes**

    /api/user/new       ==> Create new user with args ?username=YOUR_USERNAME&password=YOUR_PASSWORD
    /api/user/token     ==> Get the token with args ?username=YOUR_USERNAME&password=YOUR_PASSWORD

    /api/scan           ==> Scan the domain name, you can use either token or username:password 

    eg:  
    /api/scan?host=example.com
    default port is 443 so unless you want to scan non-default port, use port=PORT_NUMBER in args


**Test**

    curl -H "X-Auth-Token: ae027250efaafacd3087085fb1ee787c" http://localhost:5000/api/scan?host=snehesh.me


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
