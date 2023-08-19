from django.apps import AppConfig



class OfficeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OfficeApp'



    def ready(self):
        import OfficeApp.signals