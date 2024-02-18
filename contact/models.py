from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


# class Units(models.Model):
#     class Meta:
#         verbose_name = 'Unidade'

#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome


# class Category(models.Model):
#     class Meta:
#         verbose_name = 'Categoria'

#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome


# class Category2(models.Model):
#     class Meta:
#         verbose_name = 'Uso do leito'
#         verbose_name_plural = 'Usos do leito'

#     nome = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nome


class Contact(models.Model):
    class Meta:
        verbose_name = 'Parto'

    unidade_de_saude_choices = \
        ("SAMU 192", "SAMU 192"), \
        ("Convênio/Particular", "Convênio/Particular"), \
        ("ESF Esplanada dos Barreiros", "ESF Esplanada dos Barreiros"), \
        ("ESF Gleba II", "ESF Gleba II"), \
        ("ESF Humaitá I, II e III", "ESF Humaitá I, II e III"), \
        ("ESF Japuí", "ESF Japuí"), \
        ("ESF Jardim Rio Branco I", "ESF Jardim Rio Branco I"), \
        ("ESF Jardim Rio Branco II e III", "ESF Jardim Rio Branco II e III"), \
        ("ESF Jardim Rio Negro", "ESF Jardim Rio Negro"), \
        ("ESF Nova São Vicente/ESF Vila Ema", "ESF Nova São Vicente/ESF Vila Ema"), \
        ("ESF Parque Continental I e II", "ESF Parque Continental I e II"), \
        ("ESF Parque São Vicente", "ESF Parque São Vicente"), \
        ("ESF Sá Catarina", "ESF Sá Catarina"), \
        ("ESF Saquaré/México 70", "ESF Saquaré/México 70"), \
        ("SAE", "SAE"), \
        ("UBS Catiapoã", "UBS Catiapoã"), \
        ("UBS Central", "UBS Central"), \
        ("UBS/EACS Pompeba", "UBS/EACS Pompeba"), \
        ("UBS/EACS Tancredo Neves", "UBS/EACS Tancredo Neves"), \
        ("UBS/ESF Jardim Guassu", "UBS/ESF Jardim Guassu"), \
        ("UBS/ESF JIP", "UBS/ESF JIP"), \
        ("UBS/ESF Náutica III", "UBS/ESF Náutica III"), \
        ("UBS/ESF Parque Bitaru", "UBS/ESF Parque Bitaru"), \
        ("UBS/ESF Parque das Bandeiras", "UBS/ESF Parque das Bandeiras"), \
        ("UBS/ESF Praça Vitória", "UBS/ESF Praça Vitória"), \
        ("UBS/ESF Samaritá", "UBS/ESF Samaritá"), \
        ("UBS/ESF Sambaiatuba", "UBS/ESF Sambaiatuba"), \
        ("UBS/ESF Vila Margarida", "UBS/ESF Vila Margarida"), \
        ("UBS/ESF Vila Ponte Nova/ESF Quarentenário", "UBS/ESF Vila Ponte Nova/ESF Quarentenário"), \
        ("Unidade de Saúde da Mulher", "Unidade de Saúde da Mulher"), \
        ("Unidade de Saúde do Adolescente", "Unidade de Saúde do Adolescente"), \
        ("Outra/Não Informado", "Outra/Não Informado"),

    data_de_internacao = models.DateField(
        auto_now=False, blank=True, null=True)
    nome_da_gestante = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento_gestante = models.DateField(
        auto_now=False, blank=True, null=True)
    idade_da_gestante = models.IntegerField(blank=True, null=True)
    municipio_de_origem = models.CharField(
        max_length=50, blank=True, null=True)
    unidade_de_saude = models.CharField(
        choices=unidade_de_saude_choices, max_length=50, blank=True)
    qtd_consultas_pre_natal = models.IntegerField(blank=True)
    procedencia = models.CharField(max_length=50, blank=True)
    peso = models.FloatField(blank=True)
    altura = models.FloatField(blank=True)
    don_g = models.IntegerField(blank=True)
    don_pn = models.IntegerField(blank=True)
    don_pc = models.IntegerField(blank=True)
    don_a = models.IntegerField(blank=True)
    ig_semanas = models.IntegerField(blank=True)
    ig_dias = models.IntegerField(blank=True)
    trabalho_de_parto = models.CharField(max_length=3, blank=True)
    bolsa = models.CharField(max_length=10, blank=True)
    strepto = models.CharField(max_length=10, blank=True)
    antibiotico = models.CharField(max_length=3, blank=True)
    plano_de_parto = models.CharField(max_length=3, blank=True)
    classificacao_de_robson = models.IntegerField(blank=True)
    hiv = models.CharField(max_length=2, blank=True)
    sifilis = models.CharField(max_length=2, blank=True)
    inducao_miso = models.CharField(max_length=3, blank=True)
    inducao_ocitocina = models.CharField(max_length=3, blank=True)
    conducao_ocitocina = models.CharField(max_length=3, blank=True)
    conducao_amniotomia = models.CharField(max_length=3, blank=True)
    tipo_de_parto = models.CharField(max_length=20, blank=True)
    perineo = models.CharField(max_length=20, blank=True)
    indicacao_episiotomia = models.CharField(max_length=3, blank=True)
    patologia = models.CharField(max_length=30, blank=True)
    bola = models.CharField(max_length=3, blank=True)
    banho = models.CharField(max_length=3, blank=True)
    deambulacao_agachamento = models.CharField(max_length=3, blank=True)
    cavalinho = models.CharField(max_length=3, blank=True)
    analgesia_no_parto = models.CharField(max_length=3, blank=True)
    acompanhante = models.CharField(max_length=3, blank=True)
    medico_obstetra = models.CharField(max_length=20, blank=True)
    enfermeira_obstetra = models.CharField(max_length=20, blank=True)
    medico_pediatra = models.CharField(max_length=20, blank=True)
    anestesista = models.CharField(max_length=20, blank=True)
    tipo_de_anestesia = models.CharField(max_length=10, blank=True)
    quem_realizou_parto = models.CharField(max_length=20, blank=True)
    indicacao_parto_cesarea = models.CharField(max_length=20, blank=True)
    indicacao_diu_lt = models.CharField(max_length=3, blank=True)
    profilaxia_ergotrate = models.CharField(max_length=3, blank=True)
    profilaxia_ocitocina = models.CharField(max_length=3, blank=True)
    profilaxia_miso = models.CharField(max_length=3, blank=True)
    profilaxia_transamin = models.CharField(max_length=3, blank=True)
    posicao_do_parto = models.CharField(max_length=20, blank=True)
    data_nascimento_rn = models.DateField(
        auto_now=False, max_length=15, blank=True)
    hora_nascimento = models.TimeField(
        auto_now=False, max_length=15, blank=True)
    apresentacao = models.CharField(max_length=15, blank=True)
    sexo_rn = models.CharField(max_length=1, blank=True)
    peso_rn = models.IntegerField(blank=True)
    pc = models.FloatField(blank=True)
    pt = models.FloatField(blank=True)
    pa = models.FloatField(blank=True)
    est = models.FloatField(blank=True)
    apgar_minuto_1 = models.IntegerField(blank=True)
    apgar_minuto_5 = models.IntegerField(blank=True)
    tax_rn = models.FloatField(blank=True)
    amamentacao_hora_1 = models.CharField(max_length=3, blank=True)
    justificativa_amamentacao = models.CharField(max_length=20, blank=True)
    contato_pele_a_pele = models.CharField(max_length=3, blank=True)
    justificativa_contato_pele_a_pele = models.CharField(
        max_length=20, blank=True)
    destino_mae = models.CharField(max_length=10, blank=True)
    destino_rn = models.CharField(max_length=10, blank=True)
    dnv = models.CharField(max_length=20, blank=True)
    baby_puff = models.CharField(max_length=3, blank=True)
    anotacoes = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    enviar_arquivo = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.nome_da_gestante} {self.data_nascimento_gestante} {self.tipo_de_parto} {self.data_nascimento_rn}'
