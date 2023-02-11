from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    #return HttpResponse("<h1 style ='background :pink'> Hello! All this is your boss SKY </h1>")
    #my_dict ={'insert_me': "I am coming from views.py file of app1"}
    my_dict = {'insert_me': "I am coming from subfolder app1_home" }
    return render(request, 'app1_home/reg.html', context= my_dict)



