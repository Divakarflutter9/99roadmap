"""
Custom validators for 99Roadmap
"""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class AlphaNumericValidator:
    """
    Validates that password contains at least one letter and one number.
    """
    
    def validate(self, password, user=None):
        has_letter = bool(re.search(r'[a-zA-Z]', password))
        has_number = bool(re.search(r'\d', password))
        
        if not (has_letter and has_number):
            raise ValidationError(
                _("Password must contain at least 8 characters, with letters and numbers combination."),
                code='password_no_alphanumeric',
            )
    
    def get_help_text(self):
        return _("Your password must contain at least one letter and one number.")
