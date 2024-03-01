from django.test import TestCase
from catalog.models import Event
from datetime import date
class EventModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Event.objects.create(title='Test Event', description='Description of the test event', date=date.today(), time='10:00', location='Test Location')

    #verify that the title field of the Event model has the correct verbose name 
    def test_title_label(self):
        event = Event.objects.get(id=1)
        field_label = event._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
    
    def test_date_is_set(self):
        # Retrieve the Event instance created in setUpTestData
        event = Event.objects.get(id=1)
        # Verify that the date field is set to today's date
        self.assertEqual(event.date, date.today())