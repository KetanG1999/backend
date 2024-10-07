from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
month_task = {
    'jan':'Lerning python',
    'feb':'Basic of python',
    'march':None,
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

def index(request):
    months = list(month_task.keys())
    return render(request,'month/index.html',{
        'monthlist':months  #(list of the months)
    })


def monthly_task_by_number(request,month):
#8000/month/1 --->8000/month/january
    months = list(month_task.keys())
    print(months)#['januay','feb','march']
    #months[0]
    if (month> len(months)):
        return HttpResponse('Invalid Month')
    redirect_month = months[month-1]
    # print(redirect_month)
    # return HttpResponseRedirect('/month/'+redirect_month) #8000/month/january
    redirect_path = reverse('month-name',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_task(request,month): #8000/january =month
    try:
        text = month_task[month]
        # responsedata = render_to_string('month/monthdetail.html')
        return render(request,'month/monthdetail.html',{
            'monthtext':text,
            'monthname': month

        })
    except:
        return HttpResponseNotFound('<h1>Invalid Month</h1>')
# Create your views here.
