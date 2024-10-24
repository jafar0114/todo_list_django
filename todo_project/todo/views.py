from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

# view menu todo list
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# view menu add to do
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})

# function delete list
def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

# function mark complete list
def mark_as_completed(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')