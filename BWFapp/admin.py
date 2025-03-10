from django.contrib import admin

from .models import FemaleSinglePlayer, MaleSinglePlayer

# Register your models here. They need to be on separate lines!
admin.site.register(FemaleSinglePlayer)
admin.site.register(MaleSinglePlayer)
