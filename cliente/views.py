from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .form import ClienteForm, VendedorForm, ServicoForm
from .models import Cliente, Vendedor, Servicos
from django.views.generic.edit import DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from .utils import render_to_pdf
import datetime

from django.template.loader import render_to_string, get_template
from weasyprint import HTML, CSS
import tempfile


# Create your views here.
#def home(request):
#   return render(request, 'cliente/home.html')

#Sessão de Listagem de dados
def HTML_Servicos_PDF(request, pk):
    servicos = Servicos.objects.get(pk=pk)
    data = {
        'servicos': servicos,
    }
    return render(request, 'cliente/PDF_servico.html', data)


def home(request):
    data = {}
    servicos = Servicos.objects.all()
    clientes = Cliente.objects.all()
    vendedor = Vendedor.objects.all()
    data['vendedores'] = vendedor
    data['clientes'] = clientes
    data['servicos'] = servicos
    return render(request, 'cliente/home.html', data)

def PDF_Servicos2(request, pk):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "inline; attachment; filename=Servicos.pdf"
    #response['Content-Transfer-Encoding'] = 'binary'

    servicos = Servicos.objects.get(pk=pk)
    data = {
        'servicos': servicos,
    }

    html_string = render_to_string('cliente/PDF_servico.html', data)
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as fd:
        fd.write(result)
        fd.flush()
        fd = open(fd.name, 'rb')
        response.write(fd.read())

    return response

#class PDF_Servicos(View):
#    def get(self,request,pk,*args, **kwargs):
#        servicos = Servicos.objects.get(pk=pk)
#        data = {
#            'servicos': servicos,
#        }

#        pdf = render_to_pdf('cliente/PDF_servico.html', data)
#        return HttpResponse(pdf,content_type='application/pdf')


# Sessão de Cadastros

def cad_Cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cliente/cad_Cliente.html', {'cad_ClienteForm': form})

def cad_Vendedor(request):
    data = {}
    form = VendedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cliente/cad_Vendedor.html', {'cad_VendedorForm': form})

def cad_Servico(request):
    form = ServicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cliente/cad_Servico.html', {'cad_ServicoForm': form})

# Sessão de Edição de dados

def update_Servico(request, pk):
    up_servico = Servicos.objects.get(pk=pk) 
    form = ServicoForm(request.POST or None, instance=up_servico)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cliente/cad_Servico.html', {'cad_ServicoForm': form})

def update_Cliente(request, pk):
    up_Cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=up_Cliente)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cliente/cad_Cliente.html', {'cad_ClienteForm': form})

def update_Vendedor(request, pk):
    up_vendedor = Vendedor.objects.get(pk=pk) 
    form = VendedorForm(request.POST or None, instance=up_vendedor)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'cliente/cad_Vendedor.html', {'cad_VendedorForm': form})

#Exemplo de Apagar dados sem confirmação do Usuario

#Apaga sem confirmação 
#def delete_Servico(request, pk):
#    del_servico = get_object_or_404(Servicos, pk=pk)
#    del_servico.delete()
#    return redirect('home')
#Apaga Com confirmação


# Sessão de Deletar dados

class delete_Servico(DeleteView):
    model = Servicos
    template_name = 'cliente/form_Delete.html'
    success_url = reverse_lazy('home')

class delete_Cliente(DeleteView):
    model = Cliente
    template_name = 'cliente/form_Delete.html'
    success_url = reverse_lazy('home')

class delete_Vendedor(DeleteView):
    model = Vendedor
    template_name = 'cliente/form_Delete.html'
    success_url = reverse_lazy('home')
