from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserRouteForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import AccidentDetail, UserRoute
from django.db.models import Q


# Create your views here.

@login_required(login_url='/login')
def index(request):
	user = UserRoute.objects.get(user=request.user)

	# accident_data = AccidentDetail.objects.filter(
	# 	Q(site__icontains=user.start) |
	# 	Q(site__icontains=user.destination) |
	# 	Q(site__icontains=user.landmark1),
	# 	Q(site__icontains=user.landmark2)
	# )

	start_acc_data = AccidentDetail.objects.filter(site=user.start)
	way = AccidentDetail.objects.filter(site=user.landmark1)
	dest_acc_data = AccidentDetail.objects.filter(site=user.destination)

	context = {'start': start_acc_data, 'dest_data': dest_acc_data, 'way': way}

	return render(request, 'core/index.html', context=context)


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


@login_required(login_url='login')
def emergency_contact(request):
	return render(request, 'core/emergency_contact.html')
