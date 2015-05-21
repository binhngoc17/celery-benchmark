import eventlet
eventlet.monkey_patch()

from celery import Celery
import requests

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
BROKER_URL = 'redis://127.0.0.1:6379/1'

celery = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task()
def make_req():
    resp = requests.get('http://localhost:3000/api')
    print resp.text