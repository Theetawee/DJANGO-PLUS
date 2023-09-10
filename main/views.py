from django.shortcuts import render
from .utils import seo




# Create your views here.
def index(request):
    context=seo()
    return render(request,'main/index.html',context )