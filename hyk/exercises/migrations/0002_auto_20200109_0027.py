# Generated by Django 2.2.2 on 2020-01-09 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('exercises', '0001_initial'),
        ('information', '0003_auto_20191224_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='session_profile',
            field=models.ForeignKey(on_delete=None, related_name='session_profile', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='sessions',
            name='session_rutines',
            field=models.ForeignKey(on_delete=None, related_name='session_rutines', to='exercises.Rutine'),
        ),
        migrations.AddField(
            model_name='rutine',
            name='created_of',
            field=models.ForeignKey(on_delete=None, related_name='created_of', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='rutine',
            name='exercises',
            field=models.ManyToManyField(to='exercises.Exercises'),
        ),
        migrations.AddField(
            model_name='rutine',
            name='info_month',
            field=models.ManyToManyField(to='information.Info_Month'),
        ),
        migrations.AddField(
            model_name='rutine',
            name='info_rutine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Info_rutine'),
        ),
        migrations.AddField(
            model_name='rutine',
            name='sessions',
            field=models.ManyToManyField(help_text='this field is for register data of the day or session training with the self rutine', through='exercises.Sessions', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='created_of',
            field=models.ForeignKey(on_delete=None, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='exercise_type',
            field=models.ManyToManyField(to='exercises.ExercisesType'),
        ),
        migrations.AddField(
            model_name='exercises',
            name='instructions',
            field=models.OneToOneField(on_delete=None, to='exercises.InstructionsExercises'),
        ),
    ]