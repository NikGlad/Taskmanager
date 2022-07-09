from django.urls import path  # скопировали весь код из файла urls папки taskmanager
from.import views # обращаемся к views

urlpatterns = [
    path('', views.index),   #добавляем index
    path('about-us', views.about), #добавляем about-as
]