from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Event, Organiser, Category, EventRegistration
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django .views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Event
from .forms import EventForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .forms import EventRegistrationForm
from .models import EventRegistration
from .forms import RegistrationForm

class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

def index(request):
    '''View function for the home page of the site'''

    '''Generate counts for the home page of the site'''
    num_events = Event.objects.all().count()
    num_organisers = Organiser.objects.all().count()
    num_categories = Category.objects.all().count()
    num_registrations = EventRegistration.objects.all().count()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_events': num_events,
        'num_organisers': num_organisers,
        'num_categories': num_categories,
        'num_registrations': num_registrations,
        'num_visits': num_visits,
    }

    '''Render the HTML template index.html with the data in the context variable'''
    return render(request, 'index.html', context=context)

def events_view(request):
    # Retrieve all events from the database
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events.html', {'events': events})
def EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'

class OrganiserListView(ListView):
    model = Organiser
    template_name = 'organiser_list.html'
    context_object_name = 'organisers'

class UserEventListView(LoginRequiredMixin, ListView):
    model = EventRegistration
    template_name = 'user_event_list.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        return EventRegistration.objects.filter(user=self.request.user)

def logout(request):
    auth_logout(request)
    success_url = reverse_lazy('events_view')
class EventCreate(PermissionRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'location', 'category', 'organiser']
    permission_required = 'catalog.add_event'
    success_url = reverse_lazy('events_view')

class EventUpdate(PermissionRequiredMixin, UpdateView):
    model = Event
    fields =  ['title', 'description', 'date', 'time', 'location', 'category', 'organiser']
    permission_required = 'catalog.change_event'
    success_url = reverse_lazy('events_view')


class EventDelete(PermissionRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events_view')
    permission_required = 'catalog.delete_event'

    def form_valid(self, request, *args, **kwargs):
       self.object = self.get_object()
       success_url = self.get_success_url()
       self.object.delete()
       return HttpResponseRedirect(success_url)

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            event_registration = form.save(commit=False)
            event_registration.user = request.user
            event_registration.event = event
            event_registration.save()
            return redirect('events_view')
    else:
        form = EventRegistrationForm(initial={'event': event})
    return render(request, 'registration.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
            form = RegistrationForm()

    return render(request, 'registration/register.html', {'form':form})