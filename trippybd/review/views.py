from django.shortcuts import get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Review
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_review(request, model_name, object_id):
    if request.method == "POST":
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        # Look up the model type (e.g., 'hotel')
        ctype = ContentType.objects.get(model=model_name)
        
        Review.objects.create(
            user=request.user,
            content_type=ctype,
            object_id=object_id,
            rating=rating,
            comment=comment
        )
    # Redirects the user exactly back to where they were
    return redirect(request.META.get('HTTP_REFERER', '/'))


# --- EDIT REVIEW ---
@login_required
def edit_review(request, review_id):
    # 1. Fetch the review. 
    # The 'user=request.user' part ensures YOU are the owner.
    review = get_object_or_404(Review, id=review_id, user=request.user)
    
    if request.method == "POST":
        # 2. Extract data from the POST request
        # The strings 'rating' and 'comment' MUST match the HTML 'name' attributes
        new_rating = request.POST.get('rating')
        new_comment = request.POST.get('comment')
        
        # 3. Apply changes and save to Database
        if new_rating and new_comment:
            review.rating = int(new_rating)
            review.comment = new_comment
            review.save()
            messages.success(request, "Changes saved successfully!")
        else:
            messages.error(request, "Error: Data missing from form.")
            
    return redirect(request.META.get('HTTP_REFERER', '/'))

# --- DELETE REVIEW ---
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    messages.success(request, "Review deleted.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


from django.http import JsonResponse

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    
    if request.method == "POST":
        review.delete()
        # If it's an AJAX request, return JSON
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
            
        messages.success(request, "Review deleted.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
        
    return JsonResponse({'status': 'error'}, status=400)