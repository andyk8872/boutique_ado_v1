from django.shortcuts import render
from .models import Wishlist


def wishlist(request):
    """
        Display the wishlist.
    """    

    return render(request, 'wishlist/wishlist.html')