from django import forms
from .models import Event
from .models import EventRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image','title', 'description', 'date', 'time', 'location', 'category', 'organiser']

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']