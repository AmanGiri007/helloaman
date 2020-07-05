from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import List
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,'swagat/home.html')

@csrf_exempt
def list(request):
    item=request.POST.get('contents',None)
    if item!=None:
        List.objects.create(list_item=item)
    all_items=List.objects.all()
    lists={
        'items':all_items,
    }
    return render(request,'swagat/list.html',lists)

@csrf_exempt
def delete(request,list_id):
    List.objects.get(pk=list_id).delete()
    return HttpResponseRedirect('/lists')