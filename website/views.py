from django.shortcuts import render,redirect
from .models import userInfo,Experience
from .forms import Contacfrom


# Create your views here.

def home(request):
    user_info = userInfo.objects.all()

    context = {
        'user_info' : user_info
    }
    return render(request,'index.html',context)

def resume(request):
    ex_info = Experience.objects.all()
    context = {
        'ex_info' : ex_info
    }
    return render(request,'resume.html',context,)

def projects(request):
    return render(request,'projects.html')

def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = Contacfrom()

    return render(request,'contact.html',{'form':form})
  


