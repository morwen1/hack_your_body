# Generated by Django 2.2.2 on 2019-12-15 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20191213_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='info_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Info_Sessions'),
        ),
    ]
