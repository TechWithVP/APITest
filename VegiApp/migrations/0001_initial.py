# Generated by Django 3.0.3 on 2020-05-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userFName', models.CharField(default='', max_length=25)),
                ('userMName', models.CharField(default='', max_length=25)),
                ('userLName', models.CharField(default='', max_length=25)),
                ('userHeight', models.CharField(default='', max_length=5)),
                ('userWeight', models.CharField(default='', max_length=5)),
                ('userAadhar', models.CharField(default='0000 0000 0000 0000', max_length=16)),
                ('userState', models.CharField(default='', max_length=25)),
                ('userCity', models.CharField(default='', max_length=25)),
                ('userArea', models.CharField(default='', max_length=25)),
                ('userAddress', models.CharField(default='', max_length=300)),
                ('userMobileNumber', models.CharField(default='0123456789', max_length=10)),
                ('userEmail', models.EmailField(default='example@gmail.com', max_length=50)),
                ('userPassword', models.CharField(default='', max_length=300)),
                ('userRole', models.CharField(default='ROLE_ADMIN', max_length=10)),
                ('userImage', models.CharField(default='', max_length=300)),
                ('userDeletionStatus', models.IntegerField(default=0)),
                ('whoAdded', models.IntegerField(default=0)),
            ],
        ),
    ]
