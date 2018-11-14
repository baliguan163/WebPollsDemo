from django.contrib import admin
from .models import Question,Choice
# Register your models here.
from django.contrib import admin
from .models import Question

# from django.contrib import admin
# from .models import Question
# admin.site.register(Question)


# 通过admin.site.register(Question)语句，我们在admin站点中注册了Question模型。
# Django会自动生成一个该模型的默认表单页面。如果你想自定义该页面的外观和工作方式
# ，可以在注册对象的时候告诉Django你的自定义选项。
# 下面是一个修改admin表单默认排序方式的例子。修改polls/admin.py的代码：：
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)

# 对于只有2个字段的情况，效果看起来还不是很明显，但是如果你有一打的字段，选择一种直观的符合我们人类习惯的排序方式则非常有用。
# 还有，当表单含有大量字段的时候，你也许想将表单划分为一些字段的集合。再次修改polls/admin.py:
# from django.contrib import admin
# from .models import Question
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)
# 字段集合fieldsets中每一个元组的第一个元素是该字段集合的标题


# 如果在创建Question对象的时候就可以直接添加一些Choice，那会更好，这就是我们要说的第二种方法。下面，让我们来动手试试。
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
# admin.site.register(Question, QuestionAdmin)
# 面的代码相当于告诉Django，Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域

# 在3个插槽的最后，还有一个Add another Choice链接。点击它，又可以获得一个新的插槽。如果你想删除新增的插槽，
# 点击它最右边的灰色X图标即可。但是，默认的三个插槽不可删除。
# 这里还有点小问题。上面页面中插槽纵队排列的方式需要占据大块的页面空间，查看起来很不方便。为此，Django提供了
# 一种扁平化的显示方式，你仅仅只需要修改一下ChoiceInline继承的类为admin.TabularInline替代先前的StackedInline类
# （其实，从类名上你就能看出两种父类的区别）
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
# admin.site.register(Question, QuestionAdmin)


# 定制实例列表页面
# 通常，Django只显示__str()__方法指定的内容。但是很多时候，我们可能要同时显示一些别的内容。要实现这一目的，
# 可以使用list_display属性，它是一个由字段组成的元组，
# 其中的每一个字段都会按顺序显示在“change list”页面上，代码如下：
# # polls/admin.py
# class QuestionAdmin(admin.ModelAdmin):
#     # ...
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
# 额外的，我们把was_published_recently()方法的结果也显示出来

# 你可以点击每一列的标题，来根据这列的内容进行排序。但是was_published_recently这一列除外，不支持这种根据
# 函数输出结果进行排序的方式。同时请注意，was_published_recently这一列的列标题默认是方法的名字，内容则是
# 输出的字符串表示形式

class ChoiceInline(admin.TabularInline): # admin.TabularInline admin.StackedInline
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Django只显示__str()
    # __方法指定的内容。但是很多时候，我们可能要同时显示一些别的内容。要实现这一目的，
    # 可以使用list_display属性，它是一个由字段组成的元组，其中的每一个字段都会按顺序显示在“change
    # list”页面上，代码如下
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 我们还可以对显示结果进行过滤!使用list_filter属性，在polls / admin.py的QuestionAdmin中添加下面的代
    # 根据你选择的过滤条件的不同，Django会在面板中添加不同的过滤选项。由于pub_date是一个DateTimeField，
    # 因此Django自动添加了这些选项：“Any
    # date”, “Today”, “Past
    # 7
    # days”, “This
    # month”, “This
    # year”
    list_filter = ['pub_date']
    # 我们添加一些搜索的能力
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)


# 将Choice注册到admin站点，这很容易，修改polls/admin.py，增加下面的内容：
# from django.contrib import admin
# from .models import Choice, Question
# admin.site.register(Choice)

admin.site.register(Choice)
#
# 增加显示列    list_display = ('question_text', 'pub_date', 'was_published_recently')
# 增加过滤器    list_filter = ['pub_date']
# 添加搜索栏    search_fields = ['question_text']
