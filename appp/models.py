from django.db import models
from django.core.validators import MinLengthValidator


class Client(models.Model):
    dni = models.CharField(primary_key=True, max_length=10,
                           validators=[MinLengthValidator(10)], null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.dni, self.name)
