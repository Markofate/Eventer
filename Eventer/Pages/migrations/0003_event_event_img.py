# Generated by Django 4.2.6 on 2023-12-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_remove_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
