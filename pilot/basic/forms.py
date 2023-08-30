from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        
from django import forms

class ResponseForm(forms.Form):
    response = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your answer here...'}))

from .models import TestFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = TestFeedback
        fields = '__all__'
