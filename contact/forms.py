from django import forms


class ContactForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
