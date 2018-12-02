from django.contrib import admin

# Register your models here.
from .models import mt
#admin.site.register(mt)

class mtAdmin(admin.ModelAdmin):
	list_display = ["sqdw", "sgdd", "sbrq"]
	list_filter = ["sqdw", "sgdd", "sbrq"]
	search_fields = ['sqdw','sgdd']
	#raw_id_fields = ["sqdw",]
	date_hietatchy ="sbrq"
	#ordering = [ 'sqrq', 'sqdw']

admin.site.register(mt, mtAdmin)