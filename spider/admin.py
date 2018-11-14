from django.contrib import admin

# Register your models here.
# from spider.models import GoodsGroupbuying
from spider.models import GoodsGroupbuying




class GoodsGroupbuyingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['goods_id']}),
        (None, {'fields': ['goods_name']}),
        ('Date information', {'fields': ['goods_begin_date'], 'classes': ['collapse']}),
    ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-goods_end_date',)
    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature'
    # 设置哪些字段可以点击进入编辑界面
    # list_display_links = ('id', 'caption')
    # list_editable 设置默认可编辑字段
    # list_editable = ['machine_room_id', 'temperature']

    # fk_fields 设置显示外键字段
    # fk_fields = ('machine_room_id',)

    list_display = ('goods_id', 'goods_name', 'goods_price','group_purchase_price','group_purchase_number',
                    'inventory_number','sold_number','remain_number',
                    'generalize_short_url','commission_price','primary_categories_id','primary_categories_name')
admin.site.register(GoodsGroupbuying,GoodsGroupbuyingAdmin)


