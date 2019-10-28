from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from .models import Assistencia, Pessoa
from django.views import generic
from django.db.models import Q
from .forms import NameForm, AssistenciaForm, pesquisaAssistenciaForm, PesquisaClienteForm
from datetime import datetime, date
import logging, json
from django.core.mail import send_mail

logger=logging.getLogger(__name__)
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_assistencia_list'

    def get_queryset(self):
        """Return the last five published assistencias."""
        return Assistencia.objects.order_by('-data')[:50]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = pesquisaAssistenciaForm()
        context['formCliente'] = PesquisaClienteForm()
        return context

def detail(request, question_id):
    return render(request,'assistencias/index.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def assistencias(request):
    return render(request,'assistencias.html',{
        'entries':Assistencia.objects.all()
    })

def detalhe(request, assistencia_id):
    assistencia = Assistencia.objects.get(pk=assistencia_id)
    form = AssistenciaForm(instance=assistencia)
    logger.error(form['cliente'].value())
    logger.error(assistencia)
    return render(request,'detalhes.html',{
    'assistencia':assistencia,
    'form':form})

def atualizar(request, assistencia_id):
    if request.method == 'POST':
        assistencia = Assistencia.objects.get(pk=assistencia_id)
        form = AssistenciaForm(request.POST,instance=assistencia)
        form.save()
        send_mail(
            'Assistencia atualizada',
            'Assistencia atualizada.',
            'mlpbarreiro@gmail.com',
            ['mlpbarreiro@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("THANKS")
    else:
        return HttpResponse("NOT VALID")

def pesquisaPessoa(request):
    body = request.POST
    assistencias = Assistencia.objects.filter(cliente__nome__contains=body["nome"])
    arrayAssistencias=[]
    for assistencia in assistencias:
        object = assistencia.sendAssistencia
        arrayAssistencias.append(object)
    return JsonResponse(arrayAssistencias,safe=False)

def pesquisarAssistencia(request):
    requestForm = pesquisaAssistenciaForm(request.POST)
    try:
        dataInit = datetime.strptime(requestForm['data_init'].value(),'%Y-%m-%d')
    except ValueError:
        dataInit = date(1990,1,1)

    try:
        dataFim = datetime.strptime(requestForm['data_fim'].value(),'%Y-%m-%d')
    except ValueError:
        dataFim = date(2100,1,1)

    assistencias = Assistencia.objects.filter(cliente__nome__icontains=requestForm['cliente'].value(),
                                              funcionario__nome__icontains=requestForm['funcionario'].value(),
                                              topico__icontains=requestForm['topico'].value(),
                                              descricao__icontains=requestForm['descricao'].value(),
                                              valor__icontains=requestForm['valor'].value(),
                                              data__gte=dataInit,
                                              data__lte=dataFim
                                              )

    logger.error(assistencias)
    return render(request,'pesquisaAssistencias.html',{'assistencias':assistencias, 'formAssistencia':pesquisaAssistenciaForm(),
                                                       'formCliente':PesquisaClienteForm})

def pesquisarCliente(request):
    if 'novoCliente' in request.POST:
        if request.POST['nome']=="":
            return HttpResponse("Nome Invalido")
        else:
            form = PesquisaClienteForm(request.POST)
            form.save()
            return HttpResponse("Cliente Adicionado com sucesso")
    else:
        requestForm = PesquisaClienteForm(request.POST)
        clientes = Pessoa.objects.filter(nome__icontains=requestForm['nome'].value())
        return render(request,'pesquisaClientes.html',{'clientes':clientes,
                      'formAssistencia':pesquisaAssistenciaForm(),'formCliente':PesquisaClienteForm()})



def atualizarCliente(request,cliente_id):
    if request.method=="GET":
        cliente=Pessoa.objects.get(pk=cliente_id)
        form = PesquisaClienteForm(instance=cliente)
        logger.error(AssistenciaForm())
        return render(request,'atualizarCliente.html',{'form':form, 'cliente':cliente, 'formAssistencia':AssistenciaForm()})
    elif request.method=="POST":
        cliente = Pessoa.objects.get(pk=cliente_id)
        form = PesquisaClienteForm(request.POST,instance=cliente)
        form.save()
        return HttpResponse("Cliente Salvo")



def novaAssistencia(request,cliente_id):
    return HttpResponse("OK nova assistencia")
