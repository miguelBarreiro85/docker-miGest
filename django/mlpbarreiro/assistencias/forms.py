from django import forms
from django.forms import ModelForm
from assistencias.models import Assistencia, Pessoa

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class AssistenciaForm(ModelForm):
    class Meta:
        model = Assistencia
        fields = ['funcionario','topico','descricao','valor']

class PesquisaClienteForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['id','telefone','morada',
                  'localidade','codigo_postal']


class pesquisaAssistenciaForm(forms.Form):
    data_init = forms.DateField(required=False)
    data_fim = forms.DateField(required=False)
    funcionario = forms.CharField(label='Nome Funcionario', max_length=100,required=False)
    cliente = forms.CharField(label="Nome Cliente", max_length=100,required=False)
    topico = forms.CharField(label="Topico", max_length=100,required=False)
    descricao = forms.CharField(label="descrição texto", widget=forms.Textarea,required=False)
    valor = forms.DecimalField(required=False)



class pesquisaNome(forms.Form):
    cliente = forms.CharField(label="Nome Cliente", max_length=100,required=False)
