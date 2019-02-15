# Generated by Django 2.1.5 on 2019-02-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]