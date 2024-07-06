#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inicio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se puede importar Django. Asegúrate de que Django esté instalado en tu entorno virtual."
        ) from exc
    execute_from_command_line(sys.argv)
