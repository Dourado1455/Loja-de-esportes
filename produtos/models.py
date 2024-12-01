from django.db import models

# Modelo para Produtos
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Modelo para Nota Fiscal
class NotaFiscal(models.Model):
    numero = models.CharField(max_length=50)
    data_emissao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return f"Nota {self.numero}"

# Modelo para Clientes
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

# Modelo para Fornecedores
class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome

# Modelo para Funcionários
class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
