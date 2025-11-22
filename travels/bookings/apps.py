from django.apps import AppConfig # type: ignore


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'travels.bookings'

    def ready(self):
        import bookings.signals