# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('muscle', models.CharField(choices=[('Biceps', 'Biceps'), ('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders')], max_length=256)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Advance', 'Advance'), ('Expert', 'Expert'), ('Pro', 'Pro')], default='Beginner', max_length=256)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('video_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('street', models.CharField(blank=True, max_length=256, null=True)),
                ('telephone', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('website', models.CharField(blank=True, max_length=256, null=True)),
                ('facebook_page', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GymMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('weight', models.FloatField(default=0)),
                ('bmi', models.FloatField(default=0)),
                ('fat_percent', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('Other', 'Other'), ('Male', 'Male'), ('Female', 'Female')], default='Other', max_length=256)),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Advance', 'Advance'), ('Expert', 'Expert'), ('Pro', 'Pro')], default='Beginner', max_length=256)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainees', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_planes', to='gymmy_app.Trainee')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlanExerciseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_notes', models.TextField()),
                ('trainee_notes', models.TextField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_details', to='gymmy_app.Exercise')),
                ('training_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_details', to='gymmy_app.TrainingPlan')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlanExerciseProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('sets', models.IntegerField()),
                ('weight', models.TextField()),
                ('training_plan_exercise_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_progress', to='gymmy_app.TrainingPlanExerciseDetail')),
            ],
        ),
        migrations.AddField(
            model_name='personalprogress',
            name='trainee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_progresses', to='gymmy_app.Trainee'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='gym_machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='gymmy_app.GymMachine'),
        ),
    ]
