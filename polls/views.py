from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Question, Choice
from django.template import loader


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 1
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
     # 2
    # template = loader.get_template('polls/index.html')
    # context = {
    #  'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

# 在实际运用中，加载模板、传递参数，返回HttpResponse对象是一整套再常用不过的操作了，为了节省力气，
# Django提供了一个快捷方式：render函数，一步到位
# render()函数的第一个位置参数是请求对象（就是view函数的第一个参数），第二个位置参数是模板。
# 还可以有一个可选的第三参数，一个字典，包含需要传递给模板的数据。最后render函数返回一个经
# 过字典数据渲染过的模板封装而成的HttpResponse对象


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    # 快捷方式：get_object_or_404()
    # 就像render函数一样，Django同样为你提供了一个偷懒的方式，替代上面的多行代码，那就是get_object_or_404()
    # 方法，参考下面的代码
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)\
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
