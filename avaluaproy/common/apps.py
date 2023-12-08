from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
     # UD6.4.d añado verbose_name
    verbose_name = 'Common'
