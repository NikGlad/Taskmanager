from django.contrib import admin
from django.urls import path, include  # подключил функцию include

urlpatterns = [
    path('admin/', admin.site.urls), # переход на страницу admin
    path('', include('main.urls'))  # обращаюсь к методу include и указываю в нём, что при переходе на главную страницу переходим на файл urls.py в папку main
]
