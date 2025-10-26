from django.test import SimpleTestCase,TestCase
from django.urls import reverse
from .models import message
# Create your tests here.
class MyTests(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_message(self):
        message.objects.create(text='just a test')
        test = message.objects.get(id=1).text
        self.assertEqual(test,'just a test')