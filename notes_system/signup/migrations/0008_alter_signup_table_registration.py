# Generated by Django 3.2.2 on 2021-05-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_signup_table_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_table',
            name='registration',
            field=models.CharField(default=123, max_length=100),
        ),
    ]
