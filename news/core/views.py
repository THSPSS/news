from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')