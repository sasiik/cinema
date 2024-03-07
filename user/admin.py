from django.contrib import admin
from .models import CustomUser, Ticket

admin.site.register(CustomUser)
admin.site.register(Ticket)

# Register your models here.
