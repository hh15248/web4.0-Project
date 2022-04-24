from django.contrib import admin
from .models import Wait

class WaitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Wait, WaitAdmin)