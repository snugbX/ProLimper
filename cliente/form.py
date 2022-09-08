from django.forms import ModelForm
from django import forms
from .models import Cliente, Vendedor, Servicos

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = ['nome','CPF','CNPJ', 'telefone', 'Whatsapp', 'endereco', 'bairro', 'numero_Casa', 'CEP']

class VendedorForm(ModelForm):
	class Meta:
		model = Vendedor
		fields = ['nome','CPF','CNPJ', 'telefone', 'Whatsapp', 'Email']


class ServicoForm(ModelForm):
	data_Execucao = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
	class Meta:
		model = Servicos
		fields = ['Cliente','Vendedor','Descricao','Valor','data_Execucao', 'Status']

	#def __init__(self, *args, **kwargs):
	#	super().__init__(*args, **kwargs)
	#	status_opc = (
	#		('I','iniciado'),
	#		('F','Finalizado'),
	#		('N_I','Não iniciado'),
	#		('C_P','Com problema')
	#	)
	#	self.fields['Status'].widget.attrs.update(
    #		choices=status_opc
    #	)