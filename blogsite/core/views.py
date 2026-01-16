from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Log
from django.utils.timezone import now
from datetime import timedelta
from .forms import Form

# Create your views here.
def home(req):
    return render(req,'home.html')

def log_list(req):
    filter_type = req.GET.get("filter")
    logs = Log.objects.all()
    today = now().date()
    if filter_type == "today":
        logs  = logs.filter(date= today)
        
    elif filter_type == "7days":
        logs = logs.filter(date__gte = today - timedelta(days=7))
    elif filter_type == "30days":
        logs = logs.filter(date__gte = today - timedelta(days=30))    
    
    return render(req,"core/list.html",{"logs":logs})

def log_detail(req,pk):
    logs = Log.objects.get(pk=pk)
    return render(req,"core/log_detail.html",{"logs":logs})

def create_log(req):
    forms = Form()
    if req.method == "POST":
        form = Form(req.POST)
        if form.is_valid():
            form.save()
        return redirect("list")
    else:
        forms = Form()
        return render(req,"core/add_log.html",{"forms":forms})
    
def update_log(req,pk):
    forms = get_object_or_404(Log,pk=pk)
    form = Form(req.POST or None, instance = forms)
    if form.is_valid():
        form.save()
        return redirect("list")
    return render(req,"core/add_log.html",{"forms":form})
    
def delete_log(req,pk):
    log = get_object_or_404(Log,pk=pk)
    log.delete()
    return redirect("list")
    