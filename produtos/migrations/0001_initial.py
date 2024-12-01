# Generated by Django 5.1.3 on 2024-12-01 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('contato', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField()),
                ('cnpj', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_admissao', models.DateField()),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('data_emissao', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.cliente')),
                ('produtos', models.ManyToManyField(to='produtos.produto')),
            ],
        ),
    ]