# Generated by Django 2.2.2 on 2019-12-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info_Exercices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('cals_burn', models.IntegerField()),
                ('kmR', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Info_Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('cals_burn', models.IntegerField()),
                ('kmR', models.IntegerField()),
                ('weigth_win', models.IntegerField()),
                ('weigth_loss', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Info_rutine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('cals_burn', models.IntegerField()),
                ('kmR', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Info_Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('cals_burn', models.IntegerField()),
                ('kmR', models.IntegerField()),
                ('time', models.TimeField()),
                ('intensity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
