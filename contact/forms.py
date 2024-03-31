# from django.core.exceptions import ValidationError
from typing import Any
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
            'description',
            'category'
        )

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     # adding message validation error test
    #     # self.add_error('first_name', ValidationError(
    #     #     'Mensagem de erro teste', code='invalid'))
    #     return super().clean()

    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if first_name == 'ABC':
    #         self.add_error('first_name', ValidationError(
    #             'Campo não pode receber ABC', code='invalid'))
    #     return first_name
