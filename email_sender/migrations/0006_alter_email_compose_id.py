# Generated by Django 4.2.1 on 2023-09-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0005_alter_email_compose_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_compose',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
