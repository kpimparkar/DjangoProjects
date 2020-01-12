from django.contrib import admin

# Register your models here.
# Registering the model here means that it is available on admin gui
from .models import Posts
admin.site.register(Posts)