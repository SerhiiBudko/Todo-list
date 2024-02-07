from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )

    class Meta:
        ordering = ["done", "-created"]

    def __str__(self) -> str:
        return self.content
