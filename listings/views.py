from django.shortcuts import render, get_object_or_404
from .models import Listing, Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	"""  Returns a list of Listing objects that match the provided query data from the user.
	Only 1 filter needs to match for a listing to be returned.
	User can query by keyword, city, state, bedrooms and price.
	"""
	queryset_list = Listing.objects.order_by('-list_date')

	# Keyword
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	# City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			queryset_list = queryset_list.filter(city__iexact=city)

	# State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			queryset_list = queryset_list.filter(state__iexact=state)

	# Bedrooms
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

	# Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price)

	context = {
		'state_choices': state_choices,
		'bedroom_choices': bedroom_choices,
		'price_choices': price_choices,
		'listings': queryset_list,
		'values': request.GET,
	}

	return render(request, 'listings/search.html', context)
	