# Generated by Django 4.0 on 2021-12-07 22:37

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0004_alter_taggeditem_content_type_alter_taggeditem_tag"),
        ("triage", "0005_tool_friendly_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="filter",
            name="definition",
        ),
        migrations.RemoveField(
            model_name="filter",
            name="name",
        ),
        migrations.RemoveField(
            model_name="filter",
            name="project",
        ),
        migrations.AddField(
            model_name="filter",
            name="action",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="filter",
            name="condition",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="filter",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="finding",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
