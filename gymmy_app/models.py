from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices

LEVELS = Choices(('Beginner', 'Beginner'), ('Advance', 'Advance'), ('Expert', 'Expert'), ('Pro', 'Pro'))
GENDERS = Choices(('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female'))
MUSCLES = Choices(('Biceps', 'Biceps'), ('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders'))


class Trainee(models.Model):
    user = models.ForeignKey(User, null=True, related_name='trainees')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDERS, default=GENDERS.Other, max_length=256)
    level = models.CharField(choices=LEVELS, default=LEVELS.Beginner, max_length=256)

    def save(self, *args, **kwargs):
        super(Trainee, self).save(*args, **kwargs)
        return self


class GymMachine(models.Model):
    name = models.CharField(max_length=256)


class Gym(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    telephone = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    facebook_page = models.CharField(max_length=256, null=True, blank=True)
    gym_machines = models.ManyToManyField(GymMachine)

    def save(self, *args, **kwargs):
        super(Gym, self).save(*args, **kwargs)
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


class Exercise(models.Model):
    gym_machine = models.ForeignKey(GymMachine, related_name='exercises')
    name = models.CharField(max_length=256)
    muscle = models.CharField(choices=MUSCLES, max_length=256)
    level = models.CharField(choices=LEVELS, default=LEVELS.Beginner, max_length=256)
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
    breaks_between_exercises = models.FloatField()
    trainer_notes = models.TextField()
    trainee_notes = models.TextField()

    def save(self, *args, **kwargs):
        super(TrainingPlanExerciseDetail, self).save(*args, **kwargs)
        return self


class TrainingPlanExerciseProgress(models.Model):
    training_plan_exercise_detail = models.ForeignKey(TrainingPlanExerciseDetail, related_name='exercise_progress')
    date = models.DateField(auto_now_add=True)
    sets = models.IntegerField()
    weight = models.TextField()
    breaks_between_sets = models.FloatField()

    def save(self, *args, **kwargs):
        super(TrainingPlanExerciseProgress, self).save(*args, **kwargs)
        return self

