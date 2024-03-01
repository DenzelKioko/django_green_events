from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import OrganiserListView
from .views import UserEventListView
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    # Define URL pattern for the catalog
    path('', views.index, name='index'),
    path('events/', views.events_view, name='events_view'),
    path('organisers/', OrganiserListView.as_view(), name='organiser_list'),
    path('my-events/', UserEventListView.as_view(), name='user_event_list'),
    path('logout/', views.logout, name='logged_out'),
    path('register/', register, name='register'),

    #path('events/', EventDetailView.as_view(),name = 'event_detail')
   # Other URL patterns for your project
]

urlpatterns += [
    path('events/create/', views.EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('events/<int:event_id>/register/', views.register_event, name='register_event'),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)