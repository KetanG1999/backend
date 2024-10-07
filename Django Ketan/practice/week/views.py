from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

week_task = {
    'sunday':'weekly off',
    'monday':'install django',
    'tuesday':'intrduction of django',
    'wednsday':'anglebracket learning',
    'thersday':'move to tamplete',
    'friday':'add HTML and CSS in templete file',
    'saturday':'Rivision and communication lecture'
}

# def index(request):
#     weeks = list(week_task.keys())
#     return render(request,'week/index.week.html',{
#         'weeklist':weeks     #pass list of weeks
#     })

def weekly_task_by_number(request,week):
    weeks = list(week_task.keys())
    print(weeks)   # [sunday,monday,tuesday]
    # weeks[0]
    if (week > len(weeks)):
        return HttpResponseNotFound('week not found')
    redirect_week = weeks[week-1]

    return HttpResponseRedirect('/week/'+redirect_week) #  it gives 8000/week/sunday

    # redirect_path = reverse('week-name',args=[redirect_week])
    # return HttpResponseRedirect(redirect_path)
    # redirect_path = reverse('montth-detail', args=[redirect_month])
    #month/jan
    #return  Httpresponse

def weekly_task(request,week):
    try:
        text = week_task[week]
        # responsedata = render_to_string('week/weekdetail.html')
        return render(request,'week/weekdetail.html',{
            'weektext':text,
            'weekname': week
        })
    except:
        return HttpResponseNotFound('<h1>Invalid Week</h1>')    