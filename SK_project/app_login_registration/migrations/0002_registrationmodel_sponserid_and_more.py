# Generated by Django 5.0.6 on 2024-05-09 19:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='sponserId',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registrationmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]