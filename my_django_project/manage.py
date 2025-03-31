#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')
    try:
        from django.core.management import execute_from_command_line # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Projet Anten_Quotidien importer avec success"
             
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
