from django.apps import AppConfig


class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Parser'

    def ready(self):
        import Parser.signals
