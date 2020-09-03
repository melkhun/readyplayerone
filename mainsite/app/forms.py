from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    # salary = forms.IntegerField(required=False)
    # capital = forms.IntegerField(required=False)

    class Meta:
        model = UserProfile
        fields = ('name', 'age', 'salary', 'capital',)
