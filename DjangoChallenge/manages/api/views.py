from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from DjangoChallenge.manages.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a specific task by ID.

    list:
    Return a list of all the existing tasks.

    create:
    Create a new task instance.

    update:
    Update a task instance.

    partial_update:
    Partially update a task instance.

    destroy:
    Delete a task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(operation_summary="Get a list of tasks")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a task")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a task")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a task")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partially update a task")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a task")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
