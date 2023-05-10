from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'core/index.html', context)

#making trend list function
# using order_by()method
def trend_list(request):
    trend_lists = Listing.objects.all().order_by('-viewCount')
    context = {
        'trend_lists':trend_lists,
    }
    return render(request,'core/index.html',context)

def contact(request):
    return render(request, 'core/contact.html')