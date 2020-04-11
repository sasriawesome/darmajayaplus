from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'darmajaya.persons'
    label = 'darmajaya_persons'
    verbose_name = 'Persons'