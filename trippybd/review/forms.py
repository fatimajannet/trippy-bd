from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} Stars") for i in range(5, 0, -1)], attrs={'class': 'form-select bg-dark text-white border-secondary'}),
            'comment': forms.Textarea(attrs={'class': 'form-control bg-dark text-white border-secondary', 'rows': 3, 'placeholder': 'Share your experience...'}),
        }