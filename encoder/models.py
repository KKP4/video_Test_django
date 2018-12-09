from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from video_encoding.fields import VideoField
from video_encoding.models import Format
from video_test.tasks import encode

class Video(models.Model):
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    file = VideoField(width_field='width', height_field='height', duration_field='duration')
    format_set = GenericRelation(Format)


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['file']


@receiver(post_save, sender=Video, dispatch_uid="create_encoding_task")
def trigger_encoding(sender, instance, **kwargs):
    encode.delay(instance.pk)
