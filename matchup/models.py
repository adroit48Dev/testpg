# from django.db import models
from djongo import models

# Create your models here.

class MatchModel(models.Model):
    activity_name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class MatchContent(models.Model):
    match = models.EmbeddedField(model_container=MatchModel, null=False)

    match_image = models.FileField(blank=True)
    match_keyword = models.CharField(max_length=255)
    match_definition = models.TextField()
    objects = models.DjongoManager()
