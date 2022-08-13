from django.urls import path  # скопировали весь код из файла urls папки taskmanager
from.import views # обращаемся к views

urlpatterns = [
    path('', views.index, name='home'),   #добавляем index
    path('about', views.about, name='about'), #добавляем about-as
    path('create', views.create, name='create')
]