from django import forms
from .models import Auction_Listings


class AddListingForm(forms.ModelForm):
    class Meta:
        model = Auction_Listings
        exclude = [
            'user',
            'closed',
            'winner'
        ]
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'placeholder': "Optional Image URL",'class': 'form-control'})
        }