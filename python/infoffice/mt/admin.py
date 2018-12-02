from django.contrib import admin
from . models import mt
# from . forms import SbForm
 
# Register your models here.
 
class mtAdmin(admin.ModelAdmin):
    list_display = ['sqdw','sgdw']

admin.site.register(mt, mtAdmin)