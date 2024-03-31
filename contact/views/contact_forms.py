from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
# from django.http import Http404
# from django.db.models import Q
# from django.core.paginator import Paginator
from contact.forms import ContactForm
from contact.models import Contact
# Create your views here.


def create(request):
    form_action = reverse('create')
    context = {
        'form': ContactForm(),
        'form_action': form_action
    }
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            # to alterate something after to commit
            # contact = form.save(commit=False)
            # contact.show = True
            # contact.save()
            return redirect('update', contact_id=contact.pk)

        context = {
            'form': form,
            'form_action': form_action
        }

    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('update', args=(contact_id,))
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save()
            # to alterate something after to commit
            # contact = form.save(commit=False)
            # contact.show = True
            # contact.save()
            return redirect('update', contact_id=contact.pk)

        context = {
            'form': form,
            'form_action': form_action
        }

    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )
