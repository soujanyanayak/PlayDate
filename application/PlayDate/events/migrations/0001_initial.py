# Generated by Django 4.0.5 on 2022-07-25 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '__first__'),
        ('groups', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.TextField(blank=True, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state_name', models.TextField(blank=True, null=True)),
                ('state_code', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Publicevent',
            fields=[
                ('public_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('banner', models.ImageField(blank=True, default='default.jpg', upload_to='publicevents_banner')),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.address')),
            ],
            options={
                'db_table': 'PublicEvent',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.TextField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('banner', models.ImageField(blank=True, default=None, upload_to='publicevents_banner')),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.address')),
                ('backend_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.backendadmin')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='groups.group')),
                ('group_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='groups.groupadmin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('content', models.CharField(max_length=200)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='events.event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
