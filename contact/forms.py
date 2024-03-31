# from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description'
        )

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     # adding message validation error test
    #     # self.add_error('first_name', ValidationError(
    #     #     'Mensagem de erro teste', code='invalid'))
    #     return super().clean()