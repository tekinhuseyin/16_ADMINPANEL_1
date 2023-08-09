from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


# ----------------------------
# Product
# ----------------------------
class ProductAdmin(ModelAdmin):
    # Tablo sutunlari
    list_display = ["id", "name", "is_in_stock", "create_date", "update_date"]
    list_editable = ["is_in_stock"]
    list_display_links = ["id", "name"]
    list_filter = ["is_in_stock", "create_date", "update_date"]



admin.site.register(Product, ProductAdmin)

# ---------------------------------
# Review
# ---------------------------------
admin.site.register(Review)

