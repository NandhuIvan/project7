from django.shortcuts import render, redirect
from.models import Task
from .form import Today
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date= request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def done(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    todo=Today(request.POST or None,instance=task)
    if todo.is_valid():
        todo.save()
        return redirect('/')
    return render(request,'edit.html',{'todo':todo,'task':task})

class TaskListView(ListView):
    model=Task
    template_name='home.html'
    Context_object_name='task1'

class TaskDetailView(DetailView):
    mode=Task
    template_name='detail.html'
    Context_object_name='task'

    
