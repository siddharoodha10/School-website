# Generated by Django 3.2.7 on 2021-09-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_attendance_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='S_fee',
            field=models.IntegerField(default=1500),
        ),
    ]
