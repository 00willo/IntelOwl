# Security Stuff
from django.core.management.utils import get_random_secret_key

from ._util import get_secret
from .commons import WEB_CLIENT_DOMAIN

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("DJANGO_SECRET", None) or get_random_secret_key()

HTTPS_ENABLED = get_secret("HTTPS_ENABLED", False)
if HTTPS_ENABLED:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    WEB_CLIENT_URL = f"https://{WEB_CLIENT_DOMAIN}"
else:
    WEB_CLIENT_URL = f"http://{WEB_CLIENT_DOMAIN}"

SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
ALLOWED_HOSTS = ["*"]
