from django.db import models

class Allergy(models.Model):
    nome = models.CharField(max_length=100)
    allergia = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} - {self.allergia}"
