from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contacts


# Create your views here.
def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password']

		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username already exists')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'Email already exists')
					return redirect('register')
				else:
					user = User.objects.create_user(
						username=username,
						password=password,
						email=email,
						first_name=first_name,
						last_name=last_name,)
					user.save()
					messages.success(request, 'You are now register and can log in')
					# Redirects to login page
					return redirect('login')
		else:
			messages.error(request, 'Passwords do not match')
			return redirect('register')

	else:
		return render(request, 'accounts/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, 'Welcome! You are now Logged in')
			# Directs user to dashboard if login is successful.
			return redirect('dashboard')
		else:
			messages.error(request, 'Username or Password do not match')
			return redirect('login')
	else:

		return render(request, 'accounts/login.html')
	
def dashboard(request):
	user_contacts = Contacts.objects.order_by('-inquiry_date').filter(user_id=request.user.id)
	context = {
		'contacts':user_contacts,
	}
	return render(request, 'accounts/dashboard.html', context)


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'You are now Logged Out!' )
		return redirect('index')
