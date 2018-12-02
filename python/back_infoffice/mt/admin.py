from django.contrib import admin
from .models import MengTouBiaoShi

class MengTouBiaoShiAdmin(admin.ModelAdmin):
    list_display = ("sqdw", "gcdd","ljxh")
    list_filter =("ljxh","gcdd")
    search_fields = ("sqdw","ljxh")
    # raw_id_fields =("gcdd",)
    date_hierarchy = "bzrq"
    ordering = ['ljxh','sqdw']

# Register your models here.
admin.site.register(MengTouBiaoShi, MengTouBiaoShiAdmin)
