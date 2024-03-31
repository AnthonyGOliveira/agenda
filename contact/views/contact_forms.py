from typing import Any
from django.shortcuts import redirect, render
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
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # to alterate something after to commit
            # contact = form.save(commit=False)
            # contact.show = True
            # contact.save()
            return redirect('create')

        context = {
            'form': form
        }

    return render(request, 'contact/create.html', context)
