# Generated by Django 4.0.1 on 2022-02-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
