from django.test import Client, TestCase
from django.urls import reverse

from .models import Student


class StudentTests(TestCase):

    def setUp(self):
        self.student = student.objects.create(
            name='Harry Potter',
            institution='JK Rowling',
            course='Magic',
        )

    def test_student_listing(self):
        self.assertEqual(f'{self.student.name}', 'Harry Potter')
        self.assertEqual(f'{self.student.institution}', 'JK Rowling')
        self.assertEqual(f'{self.student.course}', 'Magic')

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_student_detail_view(self):
        response = self.client.get(self.student.get_absolute_url())
        no_response = self.client.get('/students/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'students/student_detail.html')