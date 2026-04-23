from django import forms
from .models import Wishlist

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add travel plans or notes...',
                'class': 'form-control'
            })
        }