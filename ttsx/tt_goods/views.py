from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.



def index(request):
    # return HttpResponse('首页')

    return render(request, 'tt_goods/index.html')



