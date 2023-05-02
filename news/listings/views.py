from django.shortcuts import render , redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.
# the Logic that handle the customer's action

# CRUD - create , retrieve , update , delete , list ( fetching multiple infos)

# name of the model and name of action
# request from browser
# fetching all data from database

# list view
# get listing datas and return it with dictionary 
def listing_list(request) : 
    #listing all data
    listings = Listing.objects.all()
    #creating dictionary
    context = {
        "listings" : listings
    }
    return render(request , "listings.html", context)


#retrieve (almost same as list)
def listing_retrieve(request , pk) :
    listing = Listing.objects.get(id=pk)
    context = {
        "listing" : listing
    }
    return render(request , "listing.html", context)


#create
def listing_create(request) :
    form = ListingForm()
    if request.method == "POST" :
        form = ListingForm(request.POST)
        print(request.POST )
        #check validation
        if form.is_valid():
            form.save() #SAVE DATA TO DATABASE
            return redirect("/listings")
            
    context = {
        "form" : form
    }
    return render(request, "listing_create.html", context)


#updating
def listing_update(request , pk) :
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST" :
        form = ListingForm(request.POST , instance=listing)
        print(request.POST )
        #check validation
        if form.is_valid():
            form.save() #SAVE DATA TO DATABASE
            return redirect("/listings")
            
    context = {
        "form" : form
    }
    return render(request, "listing_update.html", context)



def listing_delete(request , pk) :
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/listings")