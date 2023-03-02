from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, UserRouteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import AccidentDetail, UserRoute
from django.db.models import Q
from bs4 import BeautifulSoup
import requests

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.

@login_required(login_url='/login')
def index(request):
	# accident_data = AccidentDetail.objects.filter(
	# 	Q(site__icontains=user.start) |
	# 	Q(site__icontains=user.destination) |
	# 	Q(site__icontains=user.landmark1),
	# 	Q(site__icontains=user.landmark2)
	# )

	try:
		user = UserRoute.objects.get(user=request.user)

		start_acc_data = AccidentDetail.objects.filter(site=user.start)
		way = AccidentDetail.objects.filter(site=user.landmark1)
		dest_acc_data = AccidentDetail.objects.filter(site=user.destination)

		context = {'start': start_acc_data, 'dest_data': dest_acc_data, 'way': way}
	except:
		a = None
		context = {'start': a, 'dest_data': a, 'way': a}

	return render(request, 'core/index.html', context=context)


def sign_up(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()


			email = EmailMessage(
				"django-test-email",
				"body",
				settings.EMAIL_HOST_USER,
				["abc@gmail.com"],
			)
			email.fail_silently = False
			email.send()

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


@login_required(login_url='login')
def emergency_contact(request):
	url = "https://www.indiatoday.in/information/story/list-of-emergency-numbers-in-india-1464566-2019-02-26"
	response = requests.get(url)
	response_url = response.text
	soup = BeautifulSoup(response_url, "html.parser")

	get_contact = soup.find(name="div", class_="jsx-99cc083358cc2e2d Story_description__fq_4S description")
	contact = get_contact.find(name="ul").getText()
	context = {'contact': contact}

	return render(request, 'core/emergency_contact.html', context=context)
