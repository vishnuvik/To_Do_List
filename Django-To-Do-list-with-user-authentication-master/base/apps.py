from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

class reviewConfig(AppConfig):
    name = 'Review'

class contactConfig(AppConfig):
    name = 'contact'


