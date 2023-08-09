from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


# ----------------------------
# Product
# ----------------------------
class ProductAdmin(ModelAdmin):
    # Tablo sutunları (model field names)
    list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date']
    # Tablo üzerinde güncelleyebilme:
    list_editable = ['is_in_stock']
    # Kayda gitmek için linkleme:
    list_display_links = ['id', 'name']
    # Filtreleme (arama değil):
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # Arama:
    search_fields = ['id', 'name']
    # Default Sıralama:
    ordering = ['id'] # 'id' -> ASC, '-id' -> DESC
    # Sayfa başına kayıt sayısı:
    list_per_page = 20
    # Tümünü göster yaparken max kayıt sayısı:
    list_max_show_all = 200
    date_hierarchy = 'create_date'



admin.site.register(Product, ProductAdmin)

# ---------------------------------
# Review
# ---------------------------------
admin.site.register(Review)

