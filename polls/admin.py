from django.contrib import admin
from polls.models import  Poll,Choice

# Register your models here.
from spider.models import GoodsGroupbuying


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    
    #这就增加了一个 “筛选” 的侧边栏，让人们通过 pub_date 字段的值来筛选 changelist 显示的内容
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll,PollAdmin)


class GoodsGroupbuyingAdmin(admin.ModelAdmin):
    fields = ['goods_id', 'goods_name']


admin.site.register(GoodsGroupbuying)
