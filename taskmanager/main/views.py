from django.shortcuts import render
from django.http import HttpResponse #импортируем библиотеку


def index(request): #создаём функцию
    return render(request, 'main/index.html') # в кавычках отбражаем ссылка на HTML. то что будет отображаться
# вместо HttpResponse используем метод render

def about(request): #создаём функцию
    return render(request, "main/about.html")