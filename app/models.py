from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=100, verbose_name="UF")

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupacao")

class Areasaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Area")

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Instituicao")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Curso")
    cargahortot = models.CharField(max_length=100, verbose_name="Carga Horaria Total")
    durameses = models.CharField(max_length=100, verbose_name="meses de duracao")
    areasaber = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="area saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituicao")



class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Diciplina")
    areasaber = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="area saber")

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mae")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    data_nasc = models.DateField(max_length=100, verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupacao")

class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Periodo")
    
class Turmas(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turmas")
    

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituicao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(max_length=100, verbose_name="Inicio")
    data_termino = models.DateField(max_length=100, verbose_name="Termino")
    
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descricao")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    num_faltas = models.CharField(max_length=100, verbose_name="Faltas")


class Ocorrencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    descricao = models.CharField(max_length=100, verbose_name="Descricao")
    data = models.DateField(max_length=100, verbose_name="Data")


class Disciplina_curso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horaria")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Periodo")

class Tipoavaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipos de avaliacao")
    