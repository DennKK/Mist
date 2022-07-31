from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control'})
        self.fields['recommended'].widget.attrs.update({'class': 'form-control'})
        self.fields['rate'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Review
        fields = ["body", "recommended", "rate"]