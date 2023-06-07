from django.shortcuts import render, redirect
from django.views import View
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from django.contrib import messages


# def make_review(request):
#     """
#     Displays the review form if user is authorised.    """
 
#     return render(request, 'review/make_review.html')

def make_review(request):
    """
    Displays the review form if user is authorised.
    """
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Review posted. Wait for approval.'
                )
            return redirect('home')

    else:
        form = ReviewForm()
        context = {
            'form': form,            
            }
    return render(request, 'review/make_review.html', context)


def show_review(request):
    """
    Displays the reviews.
    """
    reviews = Review.objects.all().order_by('-created_on')
    context = {
        'reviews': reviews,
    }
    return render(request, 'review/show_review.html', context)
