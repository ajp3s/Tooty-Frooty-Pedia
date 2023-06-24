from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from WebBasicsExam.fruit.models import Fruit


def start_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

    return value


class Profile(models.Model):

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(start_with_letter_validator,
                    validators.MinLengthValidator(2),

                    ),
    )

    last_name = models.CharField(
        max_length=35,
        validators=(start_with_letter_validator,
                    validators.MinLengthValidator(1),
                    ),

        null=False,
        blank=False,

    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,


    )

    password = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )
