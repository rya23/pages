from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    if request.method == "POST":
        # Adding a task
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        # Deleting a task
        elif "delete" in request.POST:
            task_id = request.POST.get("delete")
            if task_id:
                Task.objects.get(id=task_id).delete()
        return redirect("task_list")  # Reload the page after form submission

    tasks = Task.objects.all()
    return render(request, "todo/task_list.html", {"tasks": tasks})
