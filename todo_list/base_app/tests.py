from django.contrib.auth.models import User
from django.test import TestCase

from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )
        self.task = Task.objects.create(
            user=self.user,
            title='Test task',
            description='This is a test task.',
            complete=False
        )

    def test_task_creation(self):
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(self.task.__str__(), self.task.title)

    def test_task_attributes(self):
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.title, 'Test task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertFalse(self.task.complete)
        self.assertIsNotNone(self.task.created_at)
