from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Guest !!!! Very very Good'
    h=int(date.strftime('%H'))

    if h<12:
        msg+='Morning!!!'
    elif h<16:
        msg+='AfterNoon!!!'
    elif h<21:
        msg+='Evening!!!'
    else:
        msg='Hello Guest!!! Very Very good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1>Now Server Time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
