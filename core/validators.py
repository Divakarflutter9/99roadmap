"""
Custom validators for 99Roadmap
"""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class LetterRequiredValidator:
    """
    Validates that password contains at least one letter.
    """
    
    def validate(self, password, user=None):
        has_letter = bool(re.search(r'[a-zA-Z]', password))
        
        if not has_letter:
            raise ValidationError(
                _("Password must contain at least one letter."),
                code='password_no_letter',
            )
    
    def get_help_text(self):
        return _("Your password must contain at least one letter.")
