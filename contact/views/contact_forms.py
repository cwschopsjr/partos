from django.shortcuts import get_object_or_404, render, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'data_de_internacao', 'nome_da_gestante', 'data_nascimento_gestante',
            'idade_da_gestante', 'municipio_de_origem', 'unidade_de_saude', 'qtd_consultas_pre_natal',
            'procedencia', 'peso', 'altura', 'don_g', 'don_pn', 'don_pc', 'don_a', 'ig_semanas',
            'ig_dias', 'trabalho_de_parto', 'bolsa', 'strepto', 'antibiotico', 'plano_de_parto',
            'classificacao_de_robson', 'hiv', 'sifilis', 'inducao_miso', 'inducao_ocitocina',
            'conducao_ocitocina', 'conducao_amniotomia', 'tipo_de_parto', 'perineo', 'indicacao_episiotomia',
            'patologia', 'bola', 'banho', 'deambulacao_agachamento', 'cavalinho', 'analgesia_no_parto',
            'acompanhante', 'medico_obstetra', 'enfermeira_obstetra', 'medico_pediatra', 'anestesista',
            'tipo_de_anestesia', 'quem_realizou_parto', 'indicacao_parto_cesarea', 'indicacao_diu_lt',
            'profilaxia_ergotrate', 'profilaxia_ocitocina', 'profilaxia_miso', 'profilaxia_transamin',
            'posicao_do_parto', 'data_nascimento_rn', 'hora_nascimento', 'apresentacao', 'sexo_rn', 'peso_rn',
            'pc', 'pt', 'pa', 'est', 'apgar_minuto_1', 'apgar_minuto_5', 'tax_rn', 'amamentacao_hora_1',
            'justificativa_amamentacao', 'contato_pele_a_pele', 'justificativa_contato_pele_a_pele',
            'destino_mae', 'destino_rn', 'dnv', 'baby_puff', 'anotacoes',
        )


def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {'form': ContactForm()

               }

    return render(request, 'contact/create.html', context)