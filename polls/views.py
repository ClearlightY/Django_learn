from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    # 一个快捷函数: render()
    # render函数的三个参数: 1.请求对象 2.模板名称 3.字典作为可选
    return render(request,'polls/index.html',context)
    
    # template = loader.get_template('polls/index.html')
    # context = {
    #         'latest_question_list':latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    # 抛出404错误
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response%question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

