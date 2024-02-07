from django.contrib import admin

from tasks.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created", "deadline", "done")
    list_filter = ("done", "tags")
    search_fields = ("content",)
