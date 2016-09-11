import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))


settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'pg_utils_database',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'tests.test_utils',
    )
)
django.setup()

args = [sys.argv[0], 'test']
# Current module (``tests``) and its submodules.
test_cases = '.'

# Allow accessing test options from the command line.
offset = 1
try:
    sys.argv[1]
except IndexError:
    pass
else:
    option = sys.argv[1].startswith('-')
    if not option:
        test_cases = sys.argv[1]
        offset = 2

args.append(test_cases)
# ``verbosity`` can be overwritten from command line.
args.append('--verbosity=2')
args.extend(sys.argv[offset:])

execute_from_command_line(args)
