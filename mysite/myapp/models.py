from django.db import models

# Create your models here.
class Motos(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta():
        db_table = 'motos'

    def __str__(self):
        text = "{0} ( {1} )"
        return text.format(self.marca, self.modelo)

