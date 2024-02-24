from django.db import models


class Task(models.Model):
    NEW = 'NEW'
    INPROGRESS = 'INPROGRESS'
    INREVIEW = 'INREVIEW'
    COMPLETED = 'COMPLETED'

    STATUS_CHOICES = (
        (NEW, 'Nuevo'),
        (INPROGRESS, 'En Progreso'),
        (INREVIEW, 'En Revisión'),
        (COMPLETED, 'Completado'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NEW
    )

    def __str__(self):
        return self.title
