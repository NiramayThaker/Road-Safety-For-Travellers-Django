from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserRouteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login')
def index(request):
	return render(request, 'core/index.html')


def sign_up(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

			return redirect('/')

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)


@login_required(login_url='login')
def route_form(request):
	form = UserRouteForm()
	if request.method == "POST":
		form = UserRouteForm(request.POST)
		if form.is_valid():
			route = form.save(commit=False)
			route.user = request.user
			route.save()

			return redirect('home')

	context = {'form': form}
	return render(request, 'core/route_form.html', context=context)
