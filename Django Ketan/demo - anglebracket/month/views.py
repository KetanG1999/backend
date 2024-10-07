from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

month_task = {
    'jan':'Lerning python',
    'feb':'Basic of python',
    'march':'core python',
    'april':'Advance python',
    'may':'oops concepts in python',
    'jun':'Learning Database',
    'july':'learning SQL',
    'augest':'Learning Django',
    'sep':'Learning static urls',
    'octo':'Learning anglebracket',
    'nov':'Learning on the way',
    'dec':'in progress'
}
def monthly_task_by_number(request,month):
    return HttpResponse(month)

def monthly_task(request,month):
    try:
        text = month_task[month]
        print(text)
        return HttpResponse(text)
    except:
        return HttpResponseNotFound('Invalid Month')
# Create your views here.
