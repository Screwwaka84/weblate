# -*- coding: utf-8 -*-
# Generated by Django 3.0.4 on 2020-03-09 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("trans", "0063_auto_20200305_2202"),
        ("lang", "0005_auto_20200212_1239"),
        ("memory", "0001_squashed_0003_auto_20180321_1554"),
    ]

    operations = [
        migrations.CreateModel(
            name="Memory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("source", models.TextField()),
                ("target", models.TextField()),
                ("origin", models.TextField()),
                ("from_file", models.BooleanField()),
                ("shared", models.BooleanField()),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.Project",
                    ),
                ),
                (
                    "source_language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memory_source_set",
                        to="lang.Language",
                    ),
                ),
                (
                    "target_language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="memory_target_set",
                        to="lang.Language",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
