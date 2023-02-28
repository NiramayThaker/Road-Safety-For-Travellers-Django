from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="home"),
	path("signup", views.sign_up, name="sign-up")
]
