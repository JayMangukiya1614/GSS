# from django.apps import AppConfig


# class JoblistingsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'JobListings'


# job_listings/apps.py

from django.apps import AppConfig

class JobListingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JobListings'

    def ready(self):
        import JobListings.signals   # Import signals when the app is ready
