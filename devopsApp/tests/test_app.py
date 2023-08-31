from django.test import TestCase, Client
from .models import Person
from django.db.utils import IntegrityError
from django.urls import reverse
# Create your tests here.
# We are going to separate tests into categories: Model tests, View tests, and other tests

# 1 - Tests for Models
class PersonModelTestCase(TestCase):
    def test_person_creation(self):
        person = Person.objects.create(
            firstname='John', lastname='Doe',
            email='john@example.com', username='johndoe'
        )
        self.assertEqual(person.firstname, 'John')
        self.assertEqual(person.lastname, 'Doe')
        self.assertEqual(person.email, 'john@example.com')
        self.assertEqual(person.username, 'johndoe')

# if there was constraint on the "username" field in order to make it unique

# class PersonModelTestCase(TestCase):
#    def test_unique_username(self):
#        Person.objects.create(
#            firstname='John', lastname='Doe',
#            email='john@example.com', username='johndoe'
#        )
#  #      with self.assertRaises(IntegrityError):
#            Person.objects.create(
#                firstname='Another', last_name='Person',
#                email='another@example.com', username='johndoe'
#            )

# 2 - Tests for Views

class UserViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        Person.objects.create(username='johndoe', firstname='John', lastname='Doe', email='john@example.com')

    def test_user_list_view(self):
        """Test the person list view."""
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'johndoe')  # Check if 'johndoe' is in the response content
        
#Look if the app loads correctly        
class AppLoadTest(TestCase):
    def test_app_loads(self):
        response = self.client.get(reverse('home_view')) 
        self.assertEqual(response.status_code, 200)
