#portfolio
#handle: _MUMINUL__ISLAM___

#code
from celery import Celery
import requests
import os


BROKER_URL=os.getenv(
    "RABBITMQ_URL",
    "amqp://celeryuser:celerypass@rabbitmq:5672//"
)
RESULT_BACKEND=os.getenv(
    "REDIS_RESULT_URL",
    "redis://redis:6379/2"
)

app=Celery(
    'task_celery_app',
    broker=BROKER_URL,
    backend=RESULT_BACKEND
    )
app.conf.result_expires=60

@app.task
def call_go_server():
    """
    Calls GO program as a Background Job
    """
    url="http://go-server:6000/count?n=5"
    try:
        response=requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"error calling go server: {e}"

