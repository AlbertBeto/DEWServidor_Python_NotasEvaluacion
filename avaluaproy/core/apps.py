from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
     # UD6.4.d añado verbose_name
    verbose_name = 'Core'
