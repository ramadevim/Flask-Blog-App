#!C:\Users\maxgen\flask1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Flask-AppBuilder==2.1.5','console_scripts','fabmanager'
__requires__ = 'Flask-AppBuilder==2.1.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Flask-AppBuilder==2.1.5', 'console_scripts', 'fabmanager')()
    )
