from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(required=True, label='Full Name')
    rating = forms.IntegerField(min_value=1,max_value=5)
    text = forms.CharField(label="Enter Your Feedback" ,widget= forms.Textarea)

