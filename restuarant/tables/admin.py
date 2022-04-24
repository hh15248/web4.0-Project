from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Table, TableAdmin)