from django.test import TestCase
from django.urls import reverse
from catalog.models import Event
from datetime import date
from datetime import time



class YourViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Event.objects.create(
            title='Test Event', 
            description='Description of the test event',
            date=date.today(),  # Set the date to today's date
            time=time(hour=12, minute=0)
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/events/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('events_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('events_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')
