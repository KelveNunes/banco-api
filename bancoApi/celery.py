import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bancoapi.settings')

app = Celery('bancoapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
@app.task
def debug_task():
    print("Celery está funcionando corretamente!")