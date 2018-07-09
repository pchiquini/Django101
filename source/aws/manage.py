#!/usr/bin/env python
import os
import sys
#!/usr/local/bin/python3 <— must be this one

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
