#coding:utf-8
from django.db import models
from django.db.models import permalink


class TypePattern(models.Model):
    nome = models.CharField(verbose_name='name', max_length=255)

    class Meta:
        verbose_name = 'Types of Pattern'
        verbose_name_plural = 'Types of Patterns'

    def __unicode__(self):
        return '%s' % self.nome

# --------------------------------------------------------------------------------------

class TypeDecision(models.Model):
    nome = models.CharField(verbose_name='name', max_length=255)

    class Meta:
        verbose_name = 'Type of Decision'
        verbose_name_plural = 'Types of Decisions'
    def __unicode__(self):
        return '%s' % self.nome

# --------------------------------------------------------------------------------------

class Pattern(models.Model):

    class Meta:
        verbose_name = 'Pattern'
        verbose_name_plural = 'Patterns'

    nome = models.CharField(verbose_name='name', max_length=255)
    aliase = models.TextField()
    contexto = models.TextField(verbose_name='context')
    problema = models.TextField(verbose_name='problem')
    vantagens = models.TextField(verbose_name='advantages')
    desvantagens = models.TextField(verbose_name='drawbacks')
    aplicabilidade = models.TextField(verbose_name='applicability')
    referencias = models.TextField(verbose_name='references')
    padroesRelacionados = models.ManyToManyField("self", blank=True, related_name='patterns', verbose_name=u'related patterns')
    tipoDePadrao = models.ForeignKey(TypePattern, related_name='tipoDePadrao_set', verbose_name='type of pattern')
    imagem = models.ImageField(verbose_name='image', upload_to="fotos", blank=True)

    def __unicode__(self):
        return '%s' % self.nome

# --------------------------------------------------------------------------------------

TIPO_ESTADO = (
            ('Suggested', 'Suggested'),
            ('Reviewed', 'Reviewed'),
            ('Approved', 'Approved'),
            ('Reject', 'Reject')
)

class Decision(models.Model):

    class Meta:
        verbose_name = 'Decision'
        verbose_name_plural = 'Decisions'

    nome = models.CharField(verbose_name='name', max_length=255)
    descricao = models.TextField(verbose_name='description')
    objetivo = models.TextField(verbose_name='goal')
    motivacao = models.TextField(verbose_name='motivation')
    tipoDeDecisao = models.ForeignKey(TypeDecision, related_name='tipoDeDecisao_set', verbose_name='type of decision')
    escopo = models.TextField(verbose_name='scope')
    hipoteses = models.TextField(verbose_name='hypothesis')
    restricoes = models.TextField(verbose_name='restrictions')
    alternativas = models.TextField(verbose_name='alternatives')
    implicacoes = models.TextField(verbose_name='implication')
    decisaoRelacionada = models.ManyToManyField("self", blank=True, related_name='decisions', verbose_name=u'decisões relacionadas')
    necessidades = models.TextField(verbose_name='necessity')
    notas = models.TextField(verbose_name='annotations')
    estado = models.CharField(verbose_name='state', max_length=20, choices=TIPO_ESTADO)
    padraoUtilizado = models.ManyToManyField("Pattern", blank=True, related_name='patterns', verbose_name=u'used pattern')

    def __unicode__(self):
        return '%s' % self.nome
