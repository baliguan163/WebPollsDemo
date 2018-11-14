#!/usr/bin/python
# coding=utf-8

from django.conf.urls import url
from . import views

#
# 如上例，使用{% url 'detail' %} 可以根据polls.urls 中的name='detail' 来匹配。如果在同一个project下有多个app，其中都有name='detail' 时,又该如何匹配views呢？
# 解决方法是，添加namespace到URLconf中，如在polls/urls.py 中添加： app_name = 'polls'

# 本教程例子中，只有一个app也就是polls，但是在现实中很显然会有5个、10个、更多的app同时存在一个项目中。
# Django是如何区分这些app之间的URL name呢？
# 答案是使用URLconf的命名空间。在polls/urls.py文件的开头部分，添加一个app_name的变量来指定该应用的命名空间：
#

app_name = 'polls' # 关键是这行
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



# URLconfs 中，正则表达式中的分组()作为参数传递给view，如url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
#
# 假如请求url为 polls/34/  相当于调用detail(request,question_id='34')
#
# 分别访问一下url可见调用不同的view 函数进行相应
#
# http://localhost:8000/polls/
#
# http://localhost:8000/polls/34/
# http://localhost:8000/polls/34/results/
# http://localhost:8000/polls/34/vote/
