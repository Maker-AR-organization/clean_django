# Generated by Django 4.2.11 on 2024-03-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_batterydata_boxdata_medicinedata"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="fooddata",
            name="foodbox_Value",
            field=models.CharField(blank=True, max_length=10240, null=True),
        ),
    ]
