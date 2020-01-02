from django.contrib import admin
from .models import Memory
# Register your models here.

class MemoryAdmin(admin.ModelAdmin):
    list_display = ('date_time','one_line_description','how_was_the_day',)

admin.site.register(Memory,MemoryAdmin)