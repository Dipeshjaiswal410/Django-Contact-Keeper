from django import forms
from .models import Contact

class SaveContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','address','phone','email','contact_type']

