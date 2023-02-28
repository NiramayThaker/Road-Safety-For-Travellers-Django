from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="home"),
	path("signup", views.sign_up, name="sign-up"),
	path("set-route", views.route_form, name="route-form"),
	path("emergency-contact", views.emergency_contact, name="emergency-contact")
]
