# Generated by Django 2.2 on 2022-01-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("customers", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="client_id",
            field=models.IntegerField(unique=True),
        )
    ]
