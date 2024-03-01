from django.contrib.auth.models import User  # Import the User model if not already imported
from catalog.forms import EventRegistrationForm
from catalog.models import Event
from datetime import date, time  # Import the time module
from django.test import TestCase

class EventRegistrationFormTest(TestCase):
    def test_valid_form(self):
        # Create a user
        user = User.objects.create(username='test_user')
        
        # Create an event with a valid date and time
        event = Event.objects.create(
            title='Test Event', 
            description='Description of the test event', 
            date=date.today(),
            time=time(hour=12, minute=0)  # Set a valid time (e.g., 12:00 PM)
        )

        # Create form data with valid user and event IDs
        form_data = {
            'user': user.id,
            'event': event.id,
        }

        # Create the form instance with form data
        form = EventRegistrationForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid(), form.errors)
