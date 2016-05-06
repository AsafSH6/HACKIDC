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
    birthday = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(choices=GENDERS, default=GENDERS.Other, max_length=256)
    level = models.CharField(choices=LEVELS, default=LEVELS.Beginner, max_length=256)

    def __unicode__(self):
        return '{first_name} {last_name}, {age}, {gender}, {level}'.format(first_name=self.first_name,
                                                                           last_name=self.last_name,
                                                                           age=self.age,
                                                                           gender=self.gender,
                                                                           level=self.level)

    def save(self, *args, **kwargs):
        super(Trainee, self).save(*args, **kwargs)
        return self


class GymMachine(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(GymMachine, self).save(*args, **kwargs)
        return self


class Gym(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    telephone = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    facebook_page = models.CharField(max_length=256, null=True, blank=True)
    gym_machines = models.ManyToManyField(GymMachine)

    def __unicode__(self):
        return '{name}, {city} {street}, {telephone}, {email}, {website}, {facebook_page}'.format(name=self.name,
                                                                                                  city=self.city,
                                                                                                  street=self.street,
                                                                                                  telephone=self.telephone,
                                                                                                  email=self.email,
                                                                                                  website=self.website,
                                                                                                  facebook_page=self.facebook_page)

    def save(self, *args, **kwargs):
        super(Gym, self).save(*args, **kwargs)
        return self


class PersonalProgress(models.Model):
    trainee = models.ForeignKey(Trainee, related_name='personal_progresses')
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(default=0)
    bmi = models.FloatField(default=0)
    fat_percent = models.FloatField(default=0)

    def __unicode__(self):
        return '{first_name}, {last_name}, {date}, weight: {weight}, bmi: {bmi}, fat percent: {fat_percent}'.format(
            first_name=self.trainee.first_name,
            last_name=self.trainee.last_name,
            date=self.date,
            weight=self.weight,
            bmi=self.bmi,
            fat_percent=self.fat_percent)

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

    def __unicode__(self):
        return '{name}, {gym_machine}, {muscle}, {level}, {video_url}'.format(name=self.name,
                                                                              gym_machine=self.gym_machine.name,
                                                                              muscle=self.muscle,
                                                                              level=self.level,
                                                                              video_url=self.video_url)

    def save(self, *args, **kwargs):
        super(Exercise, self).save(*args, **kwargs)
        return self


class TrainingPlan(models.Model):
    trainee = models.ForeignKey(Trainee, related_name='training_planes')
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return 'id: {id}, training plan of: {first_name} {last_name}, {date}'.format(id=self.pk,
                                                                                     first_name=self.trainee.first_name,
                                                                                     last_name=self.trainee.last_name,
                                                                                     date=self.date)

    def save(self, *args, **kwargs):
        super(TrainingPlan, self).save(*args, **kwargs)
        return self


class TrainingPlanExerciseDetail(models.Model):
    training_plan = models.ForeignKey(TrainingPlan, related_name='exercise_details')
    exercise = models.ForeignKey(Exercise, related_name='exercise_details')
    breaks_between_exercises = models.FloatField()
    trainer_notes = models.TextField()
    trainee_notes = models.TextField()

    def __unicode__(self):
        return 'exercise details: {exercise}, breaks between exercises: {breaks}'.format(exercise=unicode(self.exercise),
                                                                                         breaks=self.breaks_between_exercises)

    def save(self, *args, **kwargs):
        super(TrainingPlanExerciseDetail, self).save(*args, **kwargs)
        return self


class TrainingPlanExerciseProgress(models.Model):
    training_plan_exercise_detail = models.ForeignKey(TrainingPlanExerciseDetail, related_name='exercise_progress')
    date = models.DateField(auto_now_add=True)
    sets = models.IntegerField()
    weight = models.TextField()
    breaks_between_sets = models.FloatField()

    def __unicode__(self):
        return 'progress: {date}, sets: {sets}, weight: {weight}'.format(date=self.date,
                                                                         sets=self.sets,
                                                                         weight=self.weight)

    def save(self, *args, **kwargs):
        super(TrainingPlanExerciseProgress, self).save(*args, **kwargs)
        return self
