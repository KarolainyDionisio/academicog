from django.db import models
# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self): 
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupacao")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"


class Areasaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Area")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Areasaber"
        verbose_name_plural = "Areassaber"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Instituicao")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    def __str__(self): 
        return f"{self.nome}"
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Curso")
    cargahortot = models.CharField(max_length=100, verbose_name="Carga Horaria Total")
    durameses = models.CharField(max_length=100, verbose_name="meses de duracao")
    areasaber = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="area saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituicao")
    def __str__(self): 
        return f"{self.nome}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Diciplina")
    areasaber = models.ForeignKey(Areasaber, on_delete=models.CASCADE, verbose_name="area saber")
    def __str__(self): 
        return f"{self.nome}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mae")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupacao")
    def __str__(self): 
        return f"{self.nome}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Periodo")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turma")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituicao")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    data_inicio = models.DateField(verbose_name="Inicio")
    data_termino = models.DateField(verbose_name="Termino")
    def __str__(self): 
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_termino}"
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descricao")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    def __str__(self): 
        return f"{self.descricao}, {self.pessoa}, {self.disciplina}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    num_faltas = models.CharField(max_length=100, verbose_name="Faltas")
    def __str__(self): 
        return f"{self.curso}, {self.disciplina}, {self.pessoa}, {self.num_faltas}"
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencia"

class Ocorrencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    descricao = models.CharField(max_length=100, verbose_name="Descricao")
    data = models.DateField( verbose_name="Data")
    def __str__(self): 
        return f"{self.curso}, {self.disciplina}, {self.pessoa}, {self.descricao}, {self.data}"
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"

class Disciplina_curso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horaria")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Periodo")
    def __str__(self): 
        return f"{self.curso}, {self.carga_horaria}, {self.disciplina}, {self.periodo}"
    class Meta:
        verbose_name = "Disciplina_curso"
        verbose_name_plural = "Disciplinas_curso"

class Tipoavaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipos de avaliacao")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Tipoavaliacao"
        verbose_name_plural = "Tiposavaliacao"

