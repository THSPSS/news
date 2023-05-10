from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ['viewCount']

    def get_readonly_fields(self, request, obj=None ):
        # make all fields read-only when editing an existing object
        if obj:
            return self.readonly_fields + ['title', 'subtitle', 'date', 'author', 'content', 'image']
        return self.readonly_fields
    

# django admin
admin.site.register(Listing)
