from django.db import models

# Create your models here.
class Cliente(models.Model):
	#dados do cliente
	nome = models.CharField(max_length=255)
	CPF = models.CharField(max_length=20, unique=True)
	CNPJ = models.CharField(max_length=20, null=True, blank=True)
	#contatos
	telefone = models.CharField(max_length=30)
	Whatsapp = models.BooleanField(default=False)
	#email = models.EmailField(max_length=255)
	#logradouro
	endereco = models.CharField(max_length=255)
	bairro = models.CharField(max_length=255)
	numero_Casa = models.IntegerField(null=True, blank=True)
	CEP = models.CharField(max_length=20)

	def __str__(self):
		return self.nome


class Vendedor(models.Model):
	nome = models.CharField(max_length=255)
	CPF = models.CharField(max_length=20, unique=True)
	CNPJ = models.CharField(max_length=20, null=True, blank=True)

	telefone = models.CharField(max_length=30)
	Whatsapp = models.BooleanField(default=False)

	Email = models.EmailField(max_length=255)

	def __str__(self):
		return self.nome
		
status_opc = (('I','iniciado'),('F','Finalizado'),('N_I','Não iniciado'),('C_P','Com problema'))
class Servicos(models.Model):
	Descricao = models.CharField(max_length=400)
	Valor = models.DecimalField(max_digits=10, decimal_places=2)
	data_Solicitacao = models.DateTimeField(auto_now_add=True)      
	data_Execucao = models.DateField(null=True, blank=True)
	Status = models.CharField(max_length=4,choices=status_opc)
	Vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
	Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	def __str__(self):
		return "{} ({})".format(self.Cliente,self.Descricao)
