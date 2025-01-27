#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import os
from django.core.exceptions import ImproperlyConfigured  # если используете Django

THE_GUARDIAN_KEY = os.environ.get('THE_GUARDIAN_KEY')
if not THE_GUARDIAN_KEY:
    raise ImproperlyConfigured("Set the THE_GUARDIAN_KEY environment variable")


# Остальной код приложения
def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infostream.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
