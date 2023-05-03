from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [ 
            "title",
            "subtitle",
            "date",
            "author",
            "content",
            "image"
        ]