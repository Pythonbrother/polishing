from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class MyTests(SimpleTestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)