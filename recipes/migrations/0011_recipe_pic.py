# Generated by Django 4.2.3 on 2023-07-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0010_alter_recipe_difficulty"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="pic",
            field=models.ImageField(default="no_picture.jpeg", upload_to="recipes"),
        ),
    ]
