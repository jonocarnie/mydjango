from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'seb-c8c+1zyl1aj_$l9b^0b_peod^sn$%i#-4765^xehu!gbn+'

DEBUG = env.bool('DJANGO_DEBUG', default=True)
