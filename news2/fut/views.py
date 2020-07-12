from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    latest_list = News.objects.order_by('-pub_date')[:15]
    context = {'latest_list': latest_list}
    return render(request, 'index.html', context)
