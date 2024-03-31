from typing import Any
from django.shortcuts import render
# from django.http import Http404
# from django.db.models import Q
# from django.core.paginator import Paginator
from contact.forms import ContactForm
# Create your views here.



def create(request):
    context = {
        'form': ContactForm()
    }
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST)
        }

    return render(request, 'contact/create.html', context)
