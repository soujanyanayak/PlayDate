# Generated by Django 4.0.5 on 2022-07-16 07:23

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('groups', '0006_rename_createdate_group_create_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
