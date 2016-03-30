from __future__ import unicode_literals
from django.db import models

# ======================
#   Cities and Comedians Tables
# =======================

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

# ======================
#   Rappers
# =======================

class Rapper(models.Model):
    name = models.CharField(max_length=100)
    records_dropped = models.IntegerField()
    rap_battles_won = models.IntegerField()
    money_spent_on_strippers_2014 = models.IntegerField()
    money_spent_on_strippers_2015 = models.IntegerField()
    gold_chains_owned = models.IntegerField()

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    rapper = models.CharField(max_length=100)
    copies_sold_first_week = models.IntegerField()
    quality_score = models.IntegerField()

    def __unicode__(self):
        return self.name

class NightClub(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    top_spender = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

# ======================
#   Questions
# =======================

class LessonQuestions(models.Model):

    level = models.CharField(max_length=100)
    lesson = models.CharField(max_length=100)
    question_no = models.IntegerField()
    question = models.CharField(max_length=1000)
    answer_query = models.CharField(max_length=2000)
    hint = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.question

