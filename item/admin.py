from django.contrib import admin

from .models import Category, Item

admin.site.site_header = '贩卖快乐'  # 设置header
admin.site.site_title = '贩卖快乐'  # 设置title
admin.site.index_title = '欢迎来使用后台'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'description',
        'price',
        'image',
        'is_sold',
        'created_by',
        'created_at',
    )
    list_filter = ('category', 'is_sold', 'created_by', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'