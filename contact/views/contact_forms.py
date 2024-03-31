from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
# Create your views here.


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

    def clean(self):
        cleaned_data = self.cleaned_data
        # adding message validation error test
        # self.add_error('first_name', ValidationError(
        #     'Mensagem de erro teste', code='invalid'))
        return super().clean()


def create(request):
    context = {
        'form': ContactForm()
    }
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST)
        }

    return render(request, 'contact/create.html', context)
