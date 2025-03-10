from django.db import models


class FemaleSinglePlayer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rank = models.IntegerField()
    country = models.CharField(max_length=100)
    country_image = models.ImageField(upload_to="country_images/")
    nb_tournaments = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MaleSinglePlayer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rank = models.IntegerField()
    country = models.CharField(max_length=100)
    country_image = models.ImageField(upload_to="country_images/")
    nb_tournaments = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
