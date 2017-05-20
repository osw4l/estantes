from django.db import models

# Create your models here.


class Estante(models.Model):
	codigo = models.CharField(max_length=4, unique=True)
	referencias = models.CharField(max_length=30, unique=True)
	cantidad = models.PositiveIntegerField()

