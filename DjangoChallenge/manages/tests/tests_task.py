from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from DjangoChallenge.manages.models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            state=Task.NEW
        )

    def test_str_representation(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_state_defaults_to_new(self):
        self.assertEqual(self.task.state, Task.NEW)


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Existing Task",
            description="Existing Description",
            state=Task.NEW
        )

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            "title": "New Task",
            "description": "New Description",
            "state": Task.NEW
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.latest('id').title, "New Task")
