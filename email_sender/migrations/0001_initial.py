# Generated by Django 4.2.1 on 2023-09-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('recipients', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]
