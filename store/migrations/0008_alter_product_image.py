# Generated by Django 4.0.1 on 2022-03-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default=None, upload_to="uploads/product/"),
        ),
    ]
