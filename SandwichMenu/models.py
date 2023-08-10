from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=5)
    kcal = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=20)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
