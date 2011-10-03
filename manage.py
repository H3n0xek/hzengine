#!/usr/bin/env python
import sys

from django.core.management import execute_manager
import imp
import os
try:
    imp.find_module('settings') # Assumed to be in the same directory.
    
except ImportError:    
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

# Adding applications dirs
sys.path.append(PARENT_DIR)
sys.path.append(os.path.join(PARENT_DIR, 'diario_extras'))

if __name__ == "__main__":
    execute_manager(settings)
