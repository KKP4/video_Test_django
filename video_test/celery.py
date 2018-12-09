from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video_test.settings')


app = Celery('video_test',
             broker='amqp://',
             backend='amqp://',
             include=['video_test.tasks'])


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
