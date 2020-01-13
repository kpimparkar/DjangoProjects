from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Using django signals to create user profile automatically on user creation
    def ready(self):
        import users.signal
