from django.db import models

class Planets(models.Model):
    name = models.TextField(max_length=64, unique=True, null=False)
    climate = models.TextField(null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.TextField(max_length=128, null=True)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.TextField(max_length=64, unique=True, null=False)
    birth_year = models.TextField(max_length=32, null=True)
    gender = models.TextField(max_length=32, null=True)
    eye_color = models.TextField(max_length=32, null=True)
    hair_color = models.TextField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name