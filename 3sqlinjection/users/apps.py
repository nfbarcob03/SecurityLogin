from django.apps import AppConfig
from django.db.utils import OperationalError

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from .models import User
        try:
            if not User.objects.exists():
                User.objects.bulk_create([
                    User(first_name='Alice', last_name='Smith'),
                    User(first_name='Bob', last_name='Jones'),
                    User(first_name='Charlie', last_name='Brown'),
                    User(first_name='Diana', last_name='Prince'),
                    User(first_name='Evan', last_name='Davis'),
                ])
        except OperationalError:
            pass  # DB might not be ready at first migration
