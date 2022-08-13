from django.shortcuts import render, redirect
from .models import Task
from  .forms import TaskForm

def index(request): #создаём функцию
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks}) # в кавычках отбражаем ссылка на HTML. то что будет отображаться
# вместо HttpResponse используем метод render

def about(request): #создаём функцию
    return render(request, "main/about.html")

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была не верной"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)