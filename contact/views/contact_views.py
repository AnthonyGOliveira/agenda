from django.shortcuts import render, get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {
        'contacts': contacts,
        'set_title': 'Contatos - '
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
