from django.apps import AppConfig

# A subclass of AppConfig that provides default values for the attributes of the class.
class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
