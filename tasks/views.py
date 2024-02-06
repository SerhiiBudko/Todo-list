from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task, Tag
from tasks.forms import TaskCreateFrom, TagCreateFrom


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "tasks/tasks_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateFrom
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:tasks-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateFrom
    template_name = "tasks/tasks_form.html"
    success_url = reverse_lazy("tasks:tasks-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:tasks-list")


class TaskStatusUpdateView(generic.UpdateView):
    model = Task

    @staticmethod
    def post(request, *args, **kwargs):
        task_id = kwargs.get("pk")
        task = Task.objects.get(pk=task_id)
        task.done ^= True
        task.save()
        return HttpResponseRedirect(reverse_lazy("tasks:tasks-list"))


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "tasks/tags_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateFrom
    template_name = "tasks/tags_form.html"
    success_url = reverse_lazy("tasks:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tasks/tags_form.html"
    success_url = reverse_lazy("tasks:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tags_confirm_delete.html"
    success_url = reverse_lazy("tasks:tags-list")
