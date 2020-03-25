import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "gmklt3alp^a-s_4!91=@0n33awdq*1kycu#3n!2l@-7!r%-e#3"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "example.core",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}
