from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render(request,'about/index.html')


def recent (request):
    return HttpResponse('recent')