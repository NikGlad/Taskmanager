from django.contrib import admin

from .models import Task  # показываем, что из файла models импортируем модель Task

admin.site.register(Task)  # обращаемся к admin, дальше обращаемся функции site.register и говорим, что регистрируем модель Task

