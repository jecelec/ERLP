from django.contrib     import admin
from .models.user       import User
from .models.statistics import Historico 

admin.site.register(User)
admin.site.register(Historico)