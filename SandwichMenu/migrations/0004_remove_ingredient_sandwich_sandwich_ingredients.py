# Generated by Django 4.2.4 on 2023-08-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SandwichMenu', '0003_remove_sandwich_ingredient_ingredient_sandwich'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='sandwich',
        ),
        migrations.AddField(
            model_name='sandwich',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='SandwichMenu.ingredient'),
        ),
    ]
