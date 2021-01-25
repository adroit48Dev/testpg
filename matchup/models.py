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
    match_image_one = models.FileField(blank=True)
    match_keyword_one = models.CharField(max_length=255)
    match_definition_one = models.TextField()
    match_image_two = models.FileField(blank=True)
    match_keyword_two = models.CharField(max_length=255)
    match_definition_two = models.TextField()
    match_image_three = models.FileField(blank=True)
    match_keyword_three = models.CharField(max_length=255)
    match_definition_three = models.TextField()
    match_image_four = models.FileField(blank=True)
    match_keyword_four = models.CharField(max_length=255)
    match_definition_four = models.TextField()
    objects = models.DjongoManager()

#
# class MatchImage(models.Model):
#     image_url = models.FileField(blank=True)
#
#     class Meta:
#         abstract: True
#
#
# class MatchKey(models.Model):
#     match_keywords = models.CharField(max_length=255)
#
#     class Meta:
#         abstract: True
#
#
# class MatchDef(models.Model):
#     match_definition = models.TextField()
#
#     class Meta:
#         abstract: True
#
#
# class MatchupGame(models.Model):
#     title = models.CharField(max_length=100, null=False)
#     match_images = models.ArrayField(model_container=MatchImage)
#     match_keywords = models.ArrayField(model_container=MatchKey)
#     match_definitions = models.ArrayField(model_container=MatchDef)
#     objects = models.DjongoManager()
