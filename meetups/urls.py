from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='all-meetups'), # our-domain.com/meetups
  path('<slug:meetup_slug>/success', views.registration_confirmation, name='confirm-registration'),
  path('<slug:meetup_slug>', views.meetup_details, name='meetup-details'), # our-domain.com/meetups/a-second-meetup
]