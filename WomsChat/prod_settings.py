# coding=utf-8
import os

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DATABASE_ENGINE"),
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USERNAME"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
        'TEST': {
            'NAME': os.getenv("TEST_DATABASE_NAME"),
        },
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'