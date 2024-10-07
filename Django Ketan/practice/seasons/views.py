from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseNotFound,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

seasons_list = {
    'summer':'Basically summer is start from the feb month, it works around the 4 month and envirement is very hot !',
    'winter':'winter is start from the octomber month it take a 4 month it create a cold environment',
    'rain':'rain seasonn is around 4 month duration it start from the june month and end the november month',
    'spring':'it come to the before the summer seasons',
    'autumn':'thise is come before the pre-winter'
}
def Season_int_url(request,seasonname):
    seasons_int = list(seasons_list.keys())
    if seasonname > len(seasons_int):
        return HttpResponseNotFound('Invalid season Name')
    # redirect_season = seasons_int[seasonname-1]
    # return HttpResponseRedirect('/seasonname/'+redirect_season)
    #      using the reverse function  
    redirect_season = reverse('seasonname',args=[seasons_int])
    return HttpResponseRedirect(redirect_season)

def Season_str_url(request,seasonname):
    try:
        # string_text = seasons_list[seasonname]
        # return HttpResponse(string_text)
        respondata = render_to_string('seasons/seasondeatails.html')
        return HttpResponse(respondata)
    except:
        return HttpResponseNotFound('Invalid season Name')
    
