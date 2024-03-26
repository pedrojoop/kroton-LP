#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'landing.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Abrir os arquivos de templates e estáticos
    open_files()

    execute_from_command_line(sys.argv)

def open_files():
    """Open static and template files in the browser."""
    template_path = os.path.join(os.getcwd(), 'templates')
    static_path = os.path.join(os.getcwd(), 'static')

if __name__ == '__main__':
    main()
