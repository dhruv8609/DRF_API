# Generated by Django 3.1.7 on 2021-07-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videocontent', '0003_videomodel_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
