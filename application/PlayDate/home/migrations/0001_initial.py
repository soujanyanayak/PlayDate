<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-06-29 19:12
=======
# Generated by Django 4.0.5 on 2022-06-29 18:37
>>>>>>> fcd2d8030eaf90f1f5ac6ac2a213d84cd5fb65e6

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountID', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('NON_BINARY', 'Non-Binary')], max_length=10)),
                ('dob', models.DateField(max_length=11)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='generalUser',
            fields=[
                ('trackingID', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
    ]
