from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices
from realtors.models import Realtor



# Create your views here.

def index(request):
	listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
	context = {
		'listing':listing,
	 	'bedroom_choices':bedroom_choices,
	 	'price_choices':price_choices,
	 	'state_choices':state_choices
	}
	return render(request, 'home.html', context)

def about(request):

	realtors = Realtor.objects.order_by('hire_date')
	mvp = Realtor.objects.all().filter(is_MVP=True)
	print(type(mvp))
	context = {
		'realtors':realtors,
		 'mvp': mvp,
	}
	return render(request, 'about.html', context)
