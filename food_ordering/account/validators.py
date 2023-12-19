from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r"^09[0-9]{9}$"
    message = _(
        "Enter a valid phone number. [09*********]"
    )
    flags = 0
