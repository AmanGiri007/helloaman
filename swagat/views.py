from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from .models import List
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'swagat/home.html')

@csrf_exempt
def list(request):
    n_user=request.user
    item=request.POST.get('contents',None)
    if item!=None:
        List.objects.create(list_item=item,user=n_user)
    all_items=List.objects.filter(user__username=n_user)
    lists={
        'items':all_items,
    }
    return render(request,'swagat/list.html',lists)

@csrf_exempt
def delete(request,list_id):
    if request.user.is_authenticated:
        List.objects.get(pk=list_id).delete()
        return HttpResponseRedirect('/lists')

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form=LoginForm()
        content={
            'form':form,
        }
        return render(request,'swagat/login.html',content)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('User not found.Recheck or Create new account')
        return HttpResponse("Invalid. Login Again!!!")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')
class RegisterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        form=RegisterForm()
        content={
            'form':form,
        }
        return render(request,'swagat/register.html',content)
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            new_user=User(username=username,email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/')
        return HttpResponse("Form not filled properly")
def edit(request,list_id):
    list_edit=request.POST.get('todo')
    data=List.objects.get(pk=list_id)
    data.list_item=list_edit
    data.save()
    return HttpResponseRedirect('/lists')