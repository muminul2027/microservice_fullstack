#portfolio
#handle: _MUMINUL__ISLAM___

#CODE
from task import call_go_server
from celery import Celery


def run_bg_task():
    send_task=call_go_server.delay()
    result=send_task.get(timeout=10)

    print("RESULT FROM RabbitMQ: ",result)
    return result
