# Generated by Django 3.2.7 on 2021-09-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_student_t_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='T_id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='Present', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='Class',
            field=models.CharField(default='One', max_length=30),
        ),
    ]
