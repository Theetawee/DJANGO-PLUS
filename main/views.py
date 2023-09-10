from django.shortcuts import render
from .utils import seo
from django.http import HttpResponse
import os
from pathlib import Path



def robots(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path=os.path.join(BASE_DIR,'templates','base','robots.txt')
    response=HttpResponse(open(path).read(),content_type='application/text')
    return response

def sitemap(request):
    return render(request,'base/sitemap.xml')

def custom_404_view(request,exception):
    return render(request, 'base/error.html', status=404)

def custom_500_view(request):
    return render(request, 'base/505.html', status=500)

def service_worker(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path=os.path.join(BASE_DIR,'templates','base','sw.js')
    response=HttpResponse(open(path).read(),content_type='application/javascript')
    return response

def manifest(request):
    return render(request, 'base/manifest.json', content_type='application/json')
    
def offline(request):
    return render(request,'main/offline.html' )   




# Create your views here.
def index(request):
    context=seo()
    return render(request,'main/index.html',context )