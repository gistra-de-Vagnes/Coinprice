from django.db import models

class Coin(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=10)

    def __str__(self):
        return self.name
