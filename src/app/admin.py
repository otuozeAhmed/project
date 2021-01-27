from django.contrib import admin

from .models import Data

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    
    list_display = ('superuser', 'group', 'text')
    list_filter = ('group', 'text')
    search_fields = ('group', 'text')
