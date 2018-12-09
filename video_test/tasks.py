from .celery import app
from video_encoding import tasks


@app.task
def encode(pk):
    tasks.convert_all_videos("encoder", "video", pk)
