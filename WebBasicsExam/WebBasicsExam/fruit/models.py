from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def all_alpha_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
        return value


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            all_alpha_validator,
                    )
    )

    image_url = models.URLField(
        null=False,
        blank=False,

    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

