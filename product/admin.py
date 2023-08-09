from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

# ------------------------------
# Category
# ------------------------------
admin.site.register(Category)

# ----------------------------
# Product
# ----------------------------
class ReviewInline(admin.TabularInline):
    model = Review # ForeignKey ModelName

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
    # Arama bilgilendirme yazısı: 
    search_help_text = 'Arama yapmak için burayı kullanınız.'
    # Default Sıralama:
    ordering = ['id'] # 'id' -> ASC, '-id' -> DESC
    # Sayfa başına kayıt sayısı:
    list_per_page = 20
    # Tümünü göster yaparken max kayıt sayısı:
    list_max_show_all = 200
    # Tarihe göre filtreleme başlığı:
    date_hierarchy = 'create_date' # Tarih field olmak zorunda.
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug' : ['name']}
    # Form liste görüntüleme:
    fields = (
        ('name', 'is_in_stock'),
        ('slug'),
        ('categories'),
        ('description'),
    )
    filter_horizontal=["categories"]
    '''
    # Detaylı form liste görüntüleme:
    fieldsets = (
        ('General Settings', {
            # "classes": ['wide'],
            "fields": (
                ('name', 'is_in_stock'),
                ('slug'),
            )
        }),
        ('Optional Settings', {
            "classes": ['collapse'],
            "fields": (
                ('description'),
            ),
            'description': "You can use this section for optionals settings"
        }),
    )
    '''

    inlines = [ReviewInline]

    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ("set_stock_in"), ("set_stock_out")
    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çıkar'

    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days
    
    # list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date', 'added_days_ago']
    list_display += ['added_days_ago']


admin.site.register(Product, ProductAdmin)

# ---------------------------------
# Review
# ---------------------------------

class ReviewAdmin(ModelAdmin):
    list_display = ("__str__", 'created_date')
    raw_id_fields = ('product',)


admin.site.register(Review, ReviewAdmin)



