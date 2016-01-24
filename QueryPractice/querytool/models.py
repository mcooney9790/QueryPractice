from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Cities(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Comedians(models.Model):

    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    years_exp = models.IntegerField()
    num_of_specials = models.IntegerField()

    def __unicode__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()
    balcony = models.BooleanField()

    def __unicode__(self):
        return self.name

class LessonQuestions(models.Model):

    level = models.CharField(max_length=100)
    lesson = models.CharField(max_length=100)
    question_no = models.IntegerField()
    question = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.question

