# Generated by Django 4.2.3 on 2023-07-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="recipe", name="difficulty",),
        migrations.AddField(
            model_name="recipe",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.PositiveIntegerField(help_text="In minutes"),
        ),
    ]
