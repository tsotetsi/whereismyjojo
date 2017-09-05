from project.settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '50d-f_v10t^1s*hdd(yje1jd=&ch6^b0!^ur(1h#a4tnb-kqb0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Use console backend during development.
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
