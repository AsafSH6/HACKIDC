from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices

LEVELS = Choices((0, 'Beginner'), (1, 'Advence'), (2, 'Expert'), (3, 'Pro'))
GENDERS = Choices((0, 'Other'), (1, 'Male'), (2, 'Female'))
MUSCLES = Choices((0, 'Biceps'), (1, 'Chest'), (2, 'Back'), (3, 'Shoulders'))


class Trainee(models.Model):
    user = models.ForeignKey(User, null=True, related_name='trainees')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=GENDERS, default=GENDERS.Other)
    level = models.IntegerField(choices=LEVELS, default=LEVELS.Beginner)

    def save(self, *args, **kwargs):
        super(Trainee, self).save(*args, **kwargs)
        return self


class Gyms(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    telephone = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    facebook_page = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Gyms, self).save(*args, **kwargs)
        return self


class PersonalProgress(models.Model):
    trainee = models.ForeignKey(Trainee, related_name='personal_progresses')
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    fat_percent = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        super(PersonalProgress, self).save(*args, **kwargs)
        return self


class GymMachine(models.Model):
    name = models.CharField(max_length=256)


class Exercise(models.Model):
    gym_machine = models.ForeignKey(GymMachine, related_name='exercises')
    name = models.CharField(max_length=256)
    muscle = models.IntegerField(choices=MUSCLES)
    level = models.IntegerField(choices=LEVELS, default=LEVELS.Beginner)
    description = models.CharField(max_length=512, null=True, blank=True)
    video_url = models.URLField()

    def save(self, *args, **kwargs):
        super(Exercise, self).save(*args, **kwargs)
        return self


class TrainingPlan(models.Model):
    trainee = models.ForeignKey(Trainee, related_name='training_planes')
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(TrainingPlan, self).save(*args, **kwargs)
        return self


class TrainingPlanExerciseDetail(models.Model):
    training_plan = models.ForeignKey(TrainingPlan, related_name='exercise_details')
    exercise = models.ForeignKey(Exercise, related_name='exercise_details')








