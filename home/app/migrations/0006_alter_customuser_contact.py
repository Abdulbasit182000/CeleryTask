# Generated by Django 4.2.7 on 2023-11-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_customuser_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="contact",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
