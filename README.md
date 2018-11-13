# python_web_tools
基于django的python_web_tools


创建数据库表 或 更改数据库表或字段
Django 1.7.1及以上 用以下命令
# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate

旧版本的Django 1.6及以下用
python manage.py syncdb


使用开发服务器
开发服务器，即开发时使用，一般修改代码后会自动重启，方便调试和开发，但是由于性能问题，建议只用来测试，不要用在生产环境。
python manage.py runserver
 
# 当提示端口被占用的时候，可以用其它端口：
python manage.py runserver 8001
python manage.py runserver 9999
（当然也可以kill掉占用端口的进程，具体后面有讲，此处想知道的同学可查下 lsof 命令用法）
 
# 监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）
python manage.py runserver 0.0.0.0:8000
# 如果是外网或者局域网电脑上可以用其它电脑查看开发服务器
# 访问对应的 ip加端口，比如 http://172.16.20.2:8000

清空数据库
python manage.py flush
此命令会询问是 yes 还是 no, 选择 yes 会把数据全部清空掉，只留下空表。


创建超级管理员




# 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名和密码必填
# 修改 用户密码可以用：
python manage.py changepassword username


Django 更改超级用户密码
在工程文件目录下敲入：
python manage.py shell

from django.contrib.auth.models import User
user = User.objects.get(username = 'admin')
user.set_password('123456')
user.save()
