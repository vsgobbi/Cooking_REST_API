from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default=None, help_text="This is a quick description of your recipe")
    directions = models.TextField(help_text="How to make the recipe", null=True, default=None, blank=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name


class Cooker(models.Model):

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

