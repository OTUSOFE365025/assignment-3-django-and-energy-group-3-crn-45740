############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################

from Cash_Register.scan_ui import View
from Cash_Register.controller import Controller

def main():
    #Initialize GUI
    view = View("Cash Register")
    
    #Wire controller to GUI
    controller = Controller(view)
    
    #Start GUI loop
    view.start()

if __name__ == "__main__":
    main()
    
