# Generated by Django 5.1 on 2024-08-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
