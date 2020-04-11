from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'darmajaya.accounts'
    label = 'darmajaya_accounts'
    verbose_name = 'Accounts'
