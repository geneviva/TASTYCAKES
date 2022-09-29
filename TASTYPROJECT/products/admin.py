from django.contrib import admin
from . models import cake_list
# Register your models here.

class CakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_featured','name','price')
    list_editable = ('is_featured')
admin.site.register(cake_list, CakeAdmin)