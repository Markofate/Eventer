# Generated by Django 4.2.6 on 2023-12-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_event_event_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
