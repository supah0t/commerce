from django import forms
from .models import Auction_Listings, Comment

CATEGORIES_LIST = [
    ('motors', 'Motors'),
    ('fashion', 'Fashion'),
    ('art', 'Art'),
    ('electronics', 'Electronics'),
    ('home', 'Home'),
    ('sports', 'Sports'),
    ('hobbies', 'Hobbies'),
    ('toys', 'Toys'),
    ('business', 'Business'),
    ('health', 'Health'),
    ('beauty', 'Beauty'),
    ('pets', 'Pets'),
    ('services', 'Services'),
    ('general', 'General')
]

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
            'image': forms.URLInput(attrs={'placeholder': "Optional Image URL",'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORIES_LIST, attrs={'class': 'form-control'})
        }
        
class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        
        labels = {
            'comment': ""
        }
        
class Bid_Form(forms.ModelForm):
    class Meta:
        model = Auction_Listings
        fields = [
            'starting_bid'
        ]
        
        labels = {
            'starting_bid': 'Add bid'
        }
        
        widgets = {
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'})
        }