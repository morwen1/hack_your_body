# Generated by Django 2.2.2 on 2019-12-13 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20191213_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutine',
            name='info_rutine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Info_rutine'),
        ),
    ]
