from django.contrib import admin
from .models import Event, EventRegistration,Organiser, Category

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'image')
    inlines = [EventRegistrationInline]

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')
    list_filter = ('registration_date',)
    search_fields = ('user__username', 'event__title')

@admin.register(Organiser)
class OrganiserAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'org_contact_email', 'org_website')
    search_fields = ('org_name', 'org_contact_email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
#manage the default User model in the admin

from django.contrib.auth.decorators import login_required


'''from django.contrib.auth.models import User

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User)  # Register the User model again if you want to manage users in the admin'''
