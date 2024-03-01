from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    """Model representing a category."""
    name = models.CharField( max_length=200 )

    def __str__(self):
        """String for representing the Model Object."""
        return self.name

    def get_events(self):
        """Returns all events associated with this category."""
        return Event.objects.filter(category=self)

    def get_absolute_url(self):
        """Returns the URL to access a particular category instance."""
        return reverse('categories', args=[str(self.id)])

class Organiser(models.Model):
    """Model representing an event organiser."""
    org_name = models.CharField(max_length=100)
    org_description = models.TextField(blank=True, null=True)
    org_contact_email = models.EmailField(blank=True, null=True)
    org_website = models.URLField(blank=True, null=True)

    def __str__(self):
        """String for representing the Model Object."""
        return self.org_name

class Event(models.Model):
    """Model representing an event."""
    image = models.ImageField(upload_to='event_images', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    organiser = models.ForeignKey('Organiser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model Object."""
        return f'{self.image},{self.title},{self.date}'

    def get_absolute_url(self):
        """Returns the URL to access a particular event instance."""
        return reverse('events', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ['date', 'title', 'location']
        ordering = ['category', '-date', 'time']

class EventRegistration(models.Model):
    """Model representing user registration for an event."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """String for representing the Model Object."""
        return f"{self.user.username} registered for {self.event.title}"

