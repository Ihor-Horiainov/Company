from django.contrib.auth.models import AbstractUser
from django.db import models

from company.settings import AUTH_USER_MODEL


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=6,
        choices=(
            ("Urgent", "urgent"),
            ("High", "high"),
            ("Medium", "medium"),
            ("Low", "low"),
        ),
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        blank=True
    )
    assignees = models.ManyToManyField(
        AUTH_USER_MODEL, related_name="tasks", blank=True
    )

    def __str__(self):
        return f"{self.name} deadline to {self.deadline}"


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
