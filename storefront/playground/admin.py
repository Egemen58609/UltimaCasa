from django.contrib import admin
from .models import Bieding, Home, Role, status, Gebruiker

admin.site.register(Bieding)
admin.site.register(Home)
admin.site.register(Role)
admin.site.register(status)
admin.site.register(Gebruiker)