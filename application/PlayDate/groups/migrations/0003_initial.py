# Generated by Django 4.0.5 on 2022-07-13 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joinDate', models.DateTimeField(auto_now=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('memberID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupID', models.AutoField(primary_key=True, serialize=False)),
                ('groupName', models.CharField(blank=True, default=None, max_length=64)),
                ('createDate', models.DateTimeField(auto_now=True)),
                ('groupDesc', models.TextField(blank=True, default=None, max_length=256, null=True)),
                ('groupAdminID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
