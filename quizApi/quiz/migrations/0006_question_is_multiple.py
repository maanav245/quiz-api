# Generated by Django 4.2.5 on 2023-09-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_quizresult_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_multiple',
            field=models.BooleanField(default=False),
        ),
    ]