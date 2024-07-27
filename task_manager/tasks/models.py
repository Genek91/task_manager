from django.db import models


STATUS_CHOICES = (
        ('queued', 'В очереди'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    )


class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='queued'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
