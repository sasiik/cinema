from django.contrib import admin
from .models import Event, EventLocation, Types

class EventAdmin(admin.ModelAdmin):
    exclude = ('is_available',)

admin.site.register(Event, EventAdmin)
admin.site.register(EventLocation)
admin.site.register(Types)



# Register your models here.
