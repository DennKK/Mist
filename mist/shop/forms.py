from .models import UserProductRelationship
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserProductRelationship
        fields = ["body", "recommended", "rate"]