# Generated by Django 4.2.2 on 2023-10-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_dailyattendance_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="dailyattendance",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]