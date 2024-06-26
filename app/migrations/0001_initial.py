# Generated by Django 5.0.3 on 2024-04-02 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areasaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Areasaber',
                'verbose_name_plural': 'Areassaber',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Ocupacao')),
            ],
            options={
                'verbose_name': 'Ocupacao',
                'verbose_name_plural': 'Ocupacoes',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'Periodo',
                'verbose_name_plural': 'Periodos',
            },
        ),
        migrations.CreateModel(
            name='Tipoavaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Tipos de avaliacao')),
            ],
            options={
                'verbose_name': 'Tipoavaliacao',
                'verbose_name_plural': 'Tiposavaliacao',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Turma')),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Diciplina')),
                ('areasaber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber', verbose_name='area saber')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Instituicao')),
                ('site', models.CharField(max_length=100, verbose_name='Site')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Instituicao',
                'verbose_name_plural': 'Instituicoes',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Curso')),
                ('cargahortot', models.CharField(max_length=100, verbose_name='Carga Horaria Total')),
                ('durameses', models.CharField(max_length=100, verbose_name='meses de duracao')),
                ('areasaber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber', verbose_name='area saber')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao', verbose_name='Instituicao')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina_curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.CharField(max_length=100, verbose_name='Carga Horaria')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periodo', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'Disciplina_curso',
                'verbose_name_plural': 'Disciplinas_curso',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_pai', models.CharField(max_length=100, verbose_name='Nome do pai')),
                ('nome_mae', models.CharField(max_length=100, verbose_name='Nome da Mae')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao', verbose_name='Ocupacao')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('data', models.DateField(verbose_name='Data')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Ocorrencia',
                'verbose_name_plural': 'Ocorrencias',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Inicio')),
                ('data_termino', models.DateField(verbose_name='Termino')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao', verbose_name='Instituicao')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
            },
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_faltas', models.CharField(max_length=100, verbose_name='Faltas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Frequencia',
                'verbose_name_plural': 'Frequencia',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Avaliacao',
                'verbose_name_plural': 'Avaliacoes',
            },
        ),
    ]
