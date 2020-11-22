from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals