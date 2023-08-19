from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CustomPasswordValidator:
    def __init__(self, min_length=8, require_digit=True, require_special=True):
        self.min_length = min_length
        self.require_digit = require_digit
        self.require_special = require_special

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("The password must be at least %d characters long.") % self.min_length,
                code='password_too_short'
            )

        if self.require_digit and not any(char.isdigit() for char in password):
            raise ValidationError(
                _("The password must contain at least one digit."),
                code='password_no_digit'
            )

        if self.require_special and not any(char.isalnum() for char in password):
            raise ValidationError(
                _("The password must contain at least one special character."),
                code='password_no_special'
            )

    def get_help_text(self):
        return _(
            "The password must be at least %d characters long and contain at least one digit and one special character."
        ) % self.min_length