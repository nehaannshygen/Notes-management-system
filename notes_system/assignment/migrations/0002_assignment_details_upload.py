# Generated by Django 3.2.2 on 2021-06-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment_details',
            name='upload',
            field=models.FileField(default='no file', upload_to='files/'),
        ),
    ]
