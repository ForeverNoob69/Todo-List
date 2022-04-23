from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    TODO = Todo.objects.all()
    if request.method == "POST":
        pending = request.POST["title"]
        new_todo = Todo(title=pending)
        new_todo.save()
        return redirect("/")
    return render(request, "index.html", {"todos": TODO})


def delete(request, pk):
    item = Todo.objects.get(id=pk)
    item.delete()
    return redirect("/")
