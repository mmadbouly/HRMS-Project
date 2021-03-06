# Generated by Django 2.2 on 2019-04-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('EMP_EmployeeID', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('EMP_LastName', models.CharField(max_length=255)),
                ('EMP_FirstName', models.CharField(max_length=255)),
                ('EMP_CompanyID', models.CharField(max_length=255)),
                ('EMP_EmployeeGender', models.CharField(max_length=255)),
                ('EMP_DateOfBirth', models.DateField(max_length=8)),
                ('EMP_TimeStamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
