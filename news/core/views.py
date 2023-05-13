from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.all()
    popular_lists = Listing.objects.all().order_by('-viewCount')
    context = {
        'listings': listings,
        'popular_lists' : popular_lists
    }
    return render(request, 'core/index.html', context)

#making trend list function
# using order_by()method
# def popular_list(request):
#     popular_lists = Listing.objects.all().order_by('-viewCount')
#     context = {
#         'popular_lists':popular_lists,
#     }
#     return render(request,'core/index.html',context)

def contact(request):
    return render(request, 'core/contact.html')