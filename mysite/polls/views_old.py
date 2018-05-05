#blog
'''
Blog homepage
entry detail page
Year-based archive page
Month-based archive page
Day-based archive page
comment action
'''
#poll
'''
Question index page recently few questions
Question detail page display a question 
Question results page display results for a particular question
vote action handles voting for a particular choice in a particular question
'''
#each view is represented a simple python function
#django choose a view by examining the URL that's required(the part of the url after the domain name)
#

from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#exception reutrn httpresponse http404
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
        }
    return HttpResponse(template.render(context,request))

    
    #output=','.join([q.question_txt for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    #return HttpResponse("You're looking at question %s" % qustion_id)
    queston=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question_id':question})

def results(request,question_id):
    response="you are looking  at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    #return HttpResponse("you are voting on question %s."% question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=
        question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"you did not select a choice "
            })
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

