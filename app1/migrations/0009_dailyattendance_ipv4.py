# Generated by Django 4.2.2 on 2023-10-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0008_employee_ipv4"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailyattendance",
            name="ipv4",
            field=models.CharField(default="0", max_length=100),
        ),
    ]