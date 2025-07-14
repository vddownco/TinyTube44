#!/usr/bin/python3.10

import sys
import os

# Add your project directory to the Python path
path = '/home/yourusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application

if __name__ == "__main__":
    application.run()