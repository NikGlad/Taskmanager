from django.db import models


class Task(models.Model): #Класс называем логично(Task), чтобы было понятно. Далее показываем, что мы наследуем всё от models и от Model
    title = models.CharField('Название', max_length=50) #показываем, что в табличке будет поле title, показывам, что максимальная длина поля 50символов
    task = models.TextField('Описание') #показываем, что в табличке будет поле task

    def __str__(self):     # метод __str__ создаётся для того, чтобы вывести на экран объект этого класса
        return self.title  # данная строка прописывается, чтобы выводился именно объект этого класса

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'