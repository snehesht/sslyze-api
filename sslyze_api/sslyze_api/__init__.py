from flask import Flask

app = Flask(__name__)


from celery import Celery

celery_app = Celery('sslyze_api_tasks', broker='amqp://guest@desktop.local',backend='redis://desktop.local')
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

from sslyze_api import views
