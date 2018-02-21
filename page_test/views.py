from django.shortcuts import render,HttpResponse


# Create your views here.
from .models import Areasinfo

def areas(request):
    '''地市'''
    area = Areasinfo.objects.filter(aParent_id__isnull=True)

    return render(request,'page_test/areas.html',{'area': area})