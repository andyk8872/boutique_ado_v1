from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(), required=True)

    class Meta:
        model = Review
        fields = ['product', 'review']
        widgets = {
            'review': forms.Textarea(attrs={
                'rows': '5',
                'cols': '90',
                'maxlength': '50',
            }),
        }
