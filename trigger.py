# from celery import Celery
# import requests

# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# BROKER_URL = 'redis://127.0.0.1:6379/1'
#
# celery = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

# while True:
#     celery

from tasks import make_req
count = 0
while True:
	count = 0
    while True:
        count += 1
        if count > 1000:
            break
        make_req.delay()

print 'DONE'