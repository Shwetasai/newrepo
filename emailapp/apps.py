from django.apps import AppConfig
class EmailappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emailapp'

    def ready(self):
        import emailapp.signals
