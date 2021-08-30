from django.shortcuts import render, get_object_or_404
from .models import Listing, Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	paginator = Paginator(listings, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		'listings': paged_listings
	}
	return render(request, 'listings/listings.html', context)

def listing(request, id):
	listing = get_object_or_404(Listing, id=id)
	
	
	return render(request, 'listings/listing.html', {'listing':listing})

def search(request):
	listing = Listing.objects.all()
	context = {
		'listing':listing,
	 	'bedroom_choices':bedroom_choices,
	 	'price_choices':price_choices,
	 	'state_choices':state_choices
	}
	return render(request, 'listings/search.html', context)
