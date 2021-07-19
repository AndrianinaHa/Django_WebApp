# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from .models import Employe
from .forms import EmployeCreate
from .models import TodoList, Category
from django.utils.translation import gettext as _


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


# DataFlair
def liste(request):
    shelf = Employe.objects.all()
    return render(request, 'employe/listeEmploye.html', {'shelf': shelf})


def upload(request):
    uploads = EmployeCreate()
    if request.method == 'POST':
        uploads = EmployeCreate(request.POST, request.FILES)
        if uploads.is_valid():
            uploads.save()
            return redirect('liste')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'liste'}}">reload</a>""")
    else:
        return render(request, 'employe/upload_forms.html', {'upload_forms': uploads})


def update_employe(request, employe_id):
    employe_id = int(employe_id)
    try:
        employe_sel = Employe.objects.get(id=employe_id)
    except Employe.DoesNotExist:
        return redirect('liste')
    employe_form = EmployeCreate(request.POST or None, instance=employe_sel)
    if employe_form.is_valid():
        employe_form.save()
        return redirect('liste')
    return render(request, 'employe/upload_forms.html', {'upload_forms': employe_form})


def delete_employe(request, employe_id):
    employe_id = int(employe_id)
    try:
        employe_sel = Employe.objects.get(id=employe_id)
    except Employe.DoesNotExist:
        return redirect('liste')
    employe_sel.delete()
    return redirect('liste')


# todo app
def todoap(request):  # the to do view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/todoap")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "todoapp/todoapp.html", {"todos": todos, "categories": categories})


