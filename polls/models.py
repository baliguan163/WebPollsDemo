from __future__ import unicode_literals
from django.db import models

from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# 在这个简单的投票应用中，我们将创建两个模型：Question和Choice。Question包含一个问题和一个发布日期。
# Choice包含两个字段：该选项的文本描述和该选项的投票数。每一条Choice都关联到一个Question。
# 这些都是由Python的类来体现，编写的全是Python的代码，不接触任何SQL语句。现在，编辑polls/models.py文件

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 函数was_published_recently(), 判断文章发表时间在当前一天之内
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    # 你可以点击每一列的标题，来根据这列的内容进行排序。但是was_published_recently这一列除外，
    # 不支持这种根据函数输出结果进行排序的方式。同时请注意，was_published_recently这一列的列标题默
    # 认是方法的名字，内容则是输出的字符串表示形式。
    # 可以通过给方法提供一些属性来改进输出的样式，如下面所示。注意这次修改的是polls / models.py文件，
    # 不要搞错了！主要是增加了最后面三行内容


    def __str__(self):
        return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 上面的代码非常简单明了。每一个类都是django.db.models.Model的子类。每一个字段都是Field类的一个实例，
# 例如用于保存字符数据的CharField和用于保存时间类型的DateTimeField，它们告诉Django每一个字段保存的数据类型。
#
# 每一个Field实例的名字就是字段的名字（如： question_text 或者 pub_date ）。在你的Python代码中会使用这个值，
# 你的数据库也会将这个值作为表的列名。
#
# 你也可以在每个Field中使用一个可选的第一位置参数用于提供一个人类可读的字段名，让你的模型更友好，更易读，
# 并且将被作为文档的一部分来增强代码的可读性。
#
# 一些Field类必须提供某些特定的参数。例如CharField需要你指定max_length。这不仅是数据库结构的需要，
# 同样也用于数据验证功能。
#
# 有必填参数，当然就会有可选参数，比如在votes里我们将其默认值设为0.
#
# 最后请注意，我们使用ForeignKey定义了一个外键关系。它告诉Django，每一个Choice关联到一个对应的Question
# （注意要将外键写在‘多’的一方）。Django支持通用的数据关系：一对一，多对一和多对多。

