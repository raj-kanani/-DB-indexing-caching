# Generated by Django 4.0.4 on 2022-05-19 07:58

import django.contrib.postgres.indexes
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddIndex(
            model_name='student',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='myginindex'),
        ),
    ]
