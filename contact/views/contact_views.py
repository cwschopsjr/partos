from django.shortcuts import get_object_or_404, render
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'site_title': 'Registros - ',
    }

    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.nome_da_gestante} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(request, 'contact/contact.html', context)
