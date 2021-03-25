from django import forms


class ApplicationForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
