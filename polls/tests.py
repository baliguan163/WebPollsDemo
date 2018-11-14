from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question

class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

        #
        # 根据前面章节的操作步骤下来，在Question
        # Model中有一个函数
        # was_published_recently(), 判断文章发表时间在当前一天之内。代码如
        #
        # def was_published_recently(self):
        #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #
        # 仔细检查，可发现上述函数有个bug。如果发表时间在未来呢，按照上面的代码是会返回true的，显然不对。
        #
        # 编写测试用例
        # polls / tests.py：
        # 运行测试用例
        #
        # $ python manage.py test  polls

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)