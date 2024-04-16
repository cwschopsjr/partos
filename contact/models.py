from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User


class Contact(models.Model):

    class Meta:
        verbose_name = 'Parto'

    sim_nao_choices = ("Sim", "Sim"), ("Não", "Não")

    sexo_choices = ("M", "M"), ("F", "F")

    reagente_choices = ("R", "R"), ("NR", "NR")

    procedencia_choices = ("AC", "AC"), ("PS", "PS")

    destino_choices = ("AC", "AC"), ("UTI", "UTI")

    diu_lt_choices = ("DIU", "DIU"), ("LT", "LT"), ("Não", "Não")

    partos_choices = ("Normal", "Normal"), ("Cesárea",
                                            "Cesárea"), ("Fórceps", "Fórceps")

    bolsa_choices = ("Integra", "Integra"), ("Rota", "Rota")

    apresentacao_choices = (
        "Cefálica", "Cefálica"), ("Pélvica", "Pélvica"), ("Transversa", "Transversa")

    anestesia_choices = ("Raqui", "Raqui"), ("Geral",
                                             "Geral"), ("Local", "Local"), ("Combinado", "Combinado")

    strepto_choices = ("Positivo", "Positivo"), ("Negativo",
                                                 "Negativo"), ("Desconhecido", "Desconhecido")

    ig_semanas_choices = \
        ("20", "20"), \
        ("21", "21"), \
        ("22", "22"), \
        ("23", "23"), \
        ("24", "24"), \
        ("25", "25"), \
        ("26", "26"), \
        ("27", "27"), \
        ("28", "28"), \
        ("29", "29"), \
        ("30", "30"), \
        ("31", "31"), \
        ("32", "32"), \
        ("33", "33"), \
        ("34", "34"), \
        ("35", "35"), \
        ("36", "36"), \
        ("37", "37"), \
        ("38", "38"), \
        ("39", "39"), \
        ("40", "40"), \
        ("41", "41"), \
        ("42", "42"), \

    ig_dias_choices = \
        ("1/7", "1/7"), \
        ("2/7", "2/7"), \
        ("3/7", "3/7"), \
        ("4/7", "4/7"), \
        ("5/7", "5/7"), \
        ("6/7", "6/7"), \

    don_choices = \
        ("0", "0"), \
        ("1", "1"), \
        ("2", "2"), \
        ("3", "3"), \
        ("4", "4"), \
        ("5", "5"), \
        ("6", "6"), \
        ("7", "7"), \
        ("8", "8"), \
        ("9", "9"), \
        ("10", "10"), \
        ("11", "11"), \
        ("12", "12"), \
        ("13", "13"), \
        ("14", "14"), \
        ("15", "15"), \

    robson_choices = \
        ("1", "1"), \
        ("2", "2"), \
        ("3", "3"), \
        ("4", "4"), \
        ("5", "5"), \
        ("6", "6"), \
        ("7", "7"), \
        ("8", "8"), \
        ("9", "9"), \
        ("10", "10"), \

    qtd_consultas_choices = \
        ("0", "0"), \
        ("1", "1"), \
        ("2", "2"), \
        ("3", "3"), \
        ("4", "4"), \
        ("5", "5"), \
        ("6", "6"), \
        ("7", "7"), \
        ("8", "8"), \
        ("9", "9"), \
        ("10+", "10+"),

    apgar_choices = \
        ("0", "0"), \
        ("1", "1"), \
        ("2", "2"), \
        ("3", "3"), \
        ("4", "4"), \
        ("5", "5"), \
        ("6", "6"), \
        ("7", "7"), \
        ("8", "8"), \
        ("9", "9"), \
        ("10", "10"),

    idade_gestante_choices = \
        ("11", "11"), \
        ("12", "12"), \
        ("13", "13"), \
        ("14", "14"), \
        ("15", "15"), \
        ("16", "16"), \
        ("17", "17"), \
        ("18", "18"), \
        ("19", "19"), \
        ("20", "20"), \
        ("21", "21"), \
        ("22", "22"), \
        ("23", "23"), \
        ("24", "24"), \
        ("25", "25"), \
        ("26", "26"), \
        ("27", "27"), \
        ("28", "28"), \
        ("29", "29"), \
        ("30", "30"), \
        ("31", "31"), \
        ("32", "32"), \
        ("33", "33"), \
        ("34", "34"), \
        ("35", "35"), \
        ("36", "36"), \
        ("37", "37"), \
        ("38", "38"), \
        ("39", "39"), \
        ("40", "40"), \
        ("41", "41"), \
        ("42", "42"), \
        ("43", "43"), \
        ("44", "44"), \
        ("45", "45"), \
        ("46", "46"), \
        ("47", "47"), \
        ("48", "48"), \
        ("49", "49"), \
        ("50", "50"), \
        ("51", "51"), \
        ("52", "52"), \
        ("53", "53"), \
        ("54", "54"), \
        ("55", "55"), \

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
        ("Outra/Não Informado", "Outra/Não Informado"), \
        ("Não fez Pré-natal", "Não fez Pré-natal"),

    perineo_choices = \
        ("Integro", "Integro"), \
        ("Laceração grau I", "Laceração grau I"), \
        ("Laceração grau II", "Laceração grau II"), \
        ("Laceração grau III", "Laceração grau III"), \
        ("Laceração grau IV", "Laceração grau IV"), \
        ("Episiotomia", "Episiotomia"), \

    posicao_parto_choices = \
        ("Litotomia", "Litotomia"), \
        ("DDH", "DDH"), \
        ("Agachamento/Cócoras", "Agachamento/Cócoras"), \
        ("4 apoios", "4 apoios"), \
        ("Sentada/Semi-sentada", "Sentada/Semi-sentada"), \
        ("Lateral", "Lateral"), \
        ("Banqueta", "Banqueta"), \
        ("Vertical", "Vertical"), \

    data_de_internacao = models.DateField(
        auto_now=False, blank=False, null=False, verbose_name='Data de internação')
    nome_da_gestante = models.CharField(
        default=None, max_length=50, blank=False, null=False)
    data_nascimento_gestante = models.DateField(default=None,
                                                auto_now=False, blank=False, null=False, verbose_name='DN da gestante')
    idade_da_gestante = models.CharField(
        choices=idade_gestante_choices, max_length=2, blank=False)
    municipio_de_origem = models.CharField(default=None,
                                           max_length=50, blank=False, null=False, verbose_name='Município de origem')
    unidade_de_saude = models.CharField(
        choices=unidade_de_saude_choices, max_length=50, blank=False, verbose_name='Unidade de Saúde')
    qtd_consultas_pre_natal = models.CharField(
        choices=qtd_consultas_choices, max_length=3, blank=False, verbose_name='Consultas de pré-natal')
    procedencia = models.CharField(
        choices=procedencia_choices, max_length=2, blank=False, verbose_name='Procedência')
    peso = models.FloatField(blank=False)
    altura = models.FloatField(blank=False)
    don_g = models.CharField(
        choices=don_choices, max_length=2, blank=False, verbose_name='DON (G)')
    don_pn = models.CharField(
        choices=don_choices, max_length=2, blank=False, verbose_name='DON (PN)')
    don_pc = models.CharField(
        choices=don_choices, max_length=2, blank=False, verbose_name='DON (PC)')
    don_a = models.CharField(
        choices=don_choices, max_length=2, blank=False, verbose_name='DON (A)')
    ig_semanas = models.CharField(
        choices=ig_semanas_choices, max_length=2, blank=False, verbose_name='IG (semanas)')
    ig_dias = models.CharField(
        choices=ig_dias_choices, max_length=3, blank=True, verbose_name='IG (dias)')
    trabalho_de_parto = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    bolsa = models.CharField(choices=bolsa_choices,
                             max_length=10, blank=False, null=False)
    strepto = models.CharField(
        choices=strepto_choices, max_length=25, blank=False, null=False)
    antibiotico = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Antibiótico')
    plano_de_parto = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    classificacao_de_robson = models.CharField(
        choices=robson_choices, max_length=2, blank=False, null=False, verbose_name='Classificação de Robson')
    hiv = models.CharField(choices=reagente_choices,
                           max_length=3, blank=False, null=False, verbose_name='HIV')
    sifilis = models.CharField(
        choices=reagente_choices, max_length=3, blank=False, null=False, verbose_name='Sífilis')
    inducao_miso = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Indução (Miso)')
    inducao_ocitocina = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Indução (Ocitocina)')
    conducao_ocitocina = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Condução (Ocitocina)')
    conducao_amniotomia = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Condução (Amniotomia)')
    tipo_de_parto = models.CharField(
        choices=partos_choices, max_length=20, blank=False, null=False)
    perineo = models.CharField(
        choices=perineo_choices, max_length=25, blank=False, null=False, verbose_name='Períneo')
    indicacao_episiotomia = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Indicação de Episiotomia')
    patologia = models.CharField(max_length=30, blank=True, null=True)
    bola = models.CharField(choices=sim_nao_choices,
                            max_length=3, blank=False, null=False)
    banho = models.CharField(choices=sim_nao_choices,
                             max_length=3, blank=False, null=False)
    deambulacao_agachamento = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Deambulação / Agachamento')
    cavalinho = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    analgesia_no_parto = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    acompanhante = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    medico_obstetra = models.CharField(
        max_length=20, blank=False, verbose_name='Médico Obstetra')
    enfermeira_obstetra = models.CharField(
        max_length=20, blank=True, verbose_name='Enfermeira Obstetra')
    medico_pediatra = models.CharField(
        max_length=20, blank=False, verbose_name='Médico Pediatra')
    anestesista = models.CharField(max_length=25, blank=True, null=True)
    tipo_de_anestesia = models.CharField(
        choices=anestesia_choices, max_length=25, blank=True, null=True)
    quem_realizou_parto = models.CharField(
        max_length=20, blank=False, null=False)
    indicacao_parto_cesarea = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Indicação de parto cesárea')
    indicacao_diu_lt = models.CharField(
        choices=diu_lt_choices, max_length=3, blank=False, null=False, verbose_name='Indicação de DIU ou LT')
    profilaxia_ergotrate = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Profilaxia com Ergotrate')
    profilaxia_ocitocina = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Profilaxia com Ocitocina')
    profilaxia_miso = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Profilaxia com Miso')
    profilaxia_transamin = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Profilaxia com Transamin')
    posicao_do_parto = models.CharField(
        choices=posicao_parto_choices, max_length=30, blank=False, null=False, verbose_name='Posição do parto')
    data_nascimento_rn = models.DateField(default=None,
                                          auto_now=False, max_length=15, blank=False, null=False, verbose_name='DN do RN')
    hora_nascimento = models.TimeField(
        auto_now=False, max_length=15, blank=False, null=False, verbose_name='Hora do nascimento')
    apresentacao = models.CharField(
        choices=apresentacao_choices, max_length=15, blank=False, null=False, verbose_name='Apresentação')
    sexo_rn = models.CharField(
        choices=sexo_choices, max_length=1, blank=False, null=False, verbose_name='Sexo do RN')
    peso_rn = models.IntegerField(
        blank=False, null=False, verbose_name='Peso do RN')
    pc = models.FloatField(blank=False, null=False,
                           verbose_name='Perímetro cefálico (PC)')
    pt = models.FloatField(blank=False, null=False,
                           verbose_name='Perímetro torácico (PT)')
    pa = models.FloatField(blank=False, null=False,
                           verbose_name='Perímetro abdominal (PA)')
    est = models.FloatField(blank=False, null=False,
                            verbose_name='Estatura do RN')
    apgar_minuto_1 = models.CharField(
        choices=apgar_choices, max_length=2, blank=False, null=False, verbose_name='Apgar 1º minuto')
    apgar_minuto_5 = models.CharField(
        choices=apgar_choices, max_length=2, blank=False, null=False, verbose_name='Apgar 5º minuto')
    tax_rn = models.FloatField(blank=False, null=False, verbose_name='TAX RN')
    amamentacao_hora_1 = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Amamentação na 1ª hora')
    justificativa_amamentacao = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Justificativa')
    contato_pele_a_pele = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False)
    justificativa_contato_pele_a_pele = models.CharField(
        max_length=20, blank=True, null=True, verbose_name='Justificativa')
    destino_mae = models.CharField(
        choices=destino_choices, max_length=10, blank=False, null=False, verbose_name='Destino da mãe')
    destino_rn = models.CharField(
        choices=destino_choices, max_length=10, blank=False, null=False, verbose_name='Destino do RN')
    dnv = models.CharField(max_length=20, blank=True,
                           null=True, verbose_name='DNV')
    baby_puff = models.CharField(
        choices=sim_nao_choices, max_length=3, blank=False, null=False, verbose_name='Baby Puff')
    anotacoes = models.TextField(
        blank=True, null=True, verbose_name='Anotações')
    show = models.BooleanField(default=False)
    # enviar_arquivo = models.ImageField(blank=False, upload_to='pictures/%Y/%m/')
    # owner = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.nome_da_gestante} {self.data_nascimento_gestante} {self.tipo_de_parto} {self.data_nascimento_rn}'
