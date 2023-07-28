import os
from django.shortcuts import render, reverse
import datetime as dt


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages,
    }

    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    template_name = 'app/time.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    current_time = dt.datetime.now().time().strftime("%H:%M")
    msg = f'Текущее время: {current_time}'
    context = {
        'pages': pages,
        'info': msg
    }

    return render(request, template_name, context)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    template_name = 'app/work_dir.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
    }

    workdir = ', '.join(map(str, os.listdir(path='.')))
    msg = f'Файлы, модули и пакеты рабочей директории проекта: {workdir}'
    context = {
        'pages': pages,
        'info': msg
    }

    return render(request, template_name, context)
