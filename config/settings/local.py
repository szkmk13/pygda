from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = ["*"]
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
# CORS_ORIGIN_WHITELIST = ["*"]
ALLOWED_HOSTS = ["*"]
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase.sql",
    }
}
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="secret",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts


# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_PORT = 1025
EMAIL_HOST = "localhost"
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]