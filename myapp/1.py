# Microsoft Windows [Version 6.1.7601]
# Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
#
# C:\Users\maxgen>cd flask1
#
# C:\Users\maxgen\flask1>pip install flask-bcrypt
# Requirement already satisfied: flask-bcrypt in c:\users\maxgen\appdata\local\pro
# grams\python\python37-32\lib\site-packages (0.7.1)
# Requirement already satisfied: Flask in c:\users\maxgen\appdata\local\programs\p
# ython\python37-32\lib\site-packages (from flask-bcrypt) (1.0.3)
# Requirement already satisfied: bcrypt in c:\users\maxgen\appdata\local\programs\
# python\python37-32\lib\site-packages (from flask-bcrypt) (3.1.7)
# Requirement already satisfied: Werkzeug>=0.14 in c:\users\maxgen\appdata\local\p
# rograms\python\python37-32\lib\site-packages (from Flask->flask-bcrypt) (0.15.4)
#
# Requirement already satisfied: click>=5.1 in c:\users\maxgen\appdata\local\progr
# ams\python\python37-32\lib\site-packages (from Flask->flask-bcrypt) (7.0)
# Requirement already satisfied: itsdangerous>=0.24 in c:\users\maxgen\appdata\loc
# al\programs\python\python37-32\lib\site-packages (from Flask->flask-bcrypt) (1.1
# .0)
# Requirement already satisfied: Jinja2>=2.10 in c:\users\maxgen\appdata\local\pro
# grams\python\python37-32\lib\site-packages (from Flask->flask-bcrypt) (2.10.1)
# Requirement already satisfied: six>=1.4.1 in c:\users\maxgen\appdata\local\progr
# ams\python\python37-32\lib\site-packages (from bcrypt->flask-bcrypt) (1.12.0)
# Requirement already satisfied: cffi>=1.1 in c:\users\maxgen\appdata\local\progra
# ms\python\python37-32\lib\site-packages (from bcrypt->flask-bcrypt) (1.12.3)
# Requirement already satisfied: MarkupSafe>=0.23 in c:\users\maxgen\appdata\local
# \programs\python\python37-32\lib\site-packages (from Jinja2>=2.10->Flask->flask-
# bcrypt) (1.1.1)
# Requirement already satisfied: pycparser in c:\users\maxgen\appdata\local\progra
# ms\python\python37-32\lib\site-packages (from cffi>=1.1->bcrypt->flask-bcrypt) (
# 2.19)
#
# C:\Users\maxgen\flask1>python
# Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Inte
# l)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from flask_bcrypt import Bcrypt
# >>> bcrypt=Bcrypt()
# >>> bcrypt.generate_password_hash('rama')
# b'$2b$12$nSRhl6oaK02/W5fvPMszT.Kwu7VVBYOdCR4ZtP13IdAfToEx5.ucW'
# >>> bcrypt.generate_password_hash('rama').decode('utf-8')
# '$2b$12$EIIu1GrrlP.B8cJsdPHrJewRCOWAQ0WDXUKIuE6KJAmp0D3pPyeOi'
# >>> hashed_pw=bcrypt.generate_password_hash('rama').decode('utf-8')
# >>> bcrypt.check_password_hash(hashed_pw,'rama')
# True
# >>> bcrypt.check_password_hash(hashed_pw,'ram')
# False
# >>> bcrypt.check_password_hash(hashed_pw,'rama')
# True
# >>>