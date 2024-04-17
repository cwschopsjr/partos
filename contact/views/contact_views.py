from django.shortcuts import get_object_or_404, render, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):

    context = {

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


def livro(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Registros - ',
    }

    return render(request, 'contact/livro.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:livro')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(nome_da_gestante__icontains=search_value) |
            Q(data_nascimento_gestante__icontains=search_value) |
            Q(tipo_de_parto__icontains=search_value) |
            Q(data_nascimento_rn__icontains=search_value) |
            Q(data_de_internacao__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/livro.html',
        context
    )
