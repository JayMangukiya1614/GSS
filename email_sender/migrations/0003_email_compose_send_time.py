# Generated by Django 4.2.1 on 2023-09-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0002_email_compose_delete_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_compose',
            name='send_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
