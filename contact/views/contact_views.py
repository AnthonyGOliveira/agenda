from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contacts, 10)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'set_title': 'Contatos - '
    }
    return render(request, 'contact/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('index')

    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(
        last_name__icontains=search_value) | Q(phone__icontains=search_value) | Q(email__icontains=search_value)).order_by('-id')

    paginator = Paginator(contacts, 10)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'set_title': 'Search - ',
        'search_value': search_value
    }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    # contact_single = Contact.objects.filter(pk=contact_id).first()
    contact_single = get_object_or_404(
        Contact.objects, pk=contact_id, show=True)

    # if contact_single is None:
    #     raise Http404()

    context = {
        'contact': contact_single,
        'set_title': 'Detalhes de contato - '
    }
    return render(request, 'contact/contact.html', context)
