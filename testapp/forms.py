from django import forms
from testapp.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
