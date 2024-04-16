from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'Pessoa.html', {'pessoas':pessoas})
    def post(self, request):
        pass
class AreasaberView(View):
    def get(self, request, *args, **kwargs):
        areasaber = Areasaber.objects.all()
        return render(request, 'AreaSaber.html', {'areasaber':areasaber})
    def post(self, request):
        pass

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacao = Avaliacao.objects.all()
        return render(request, 'Avaliacao.html', {'avaliacao':avaliacao})
    def post(self, request):
        pass
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'Cidade.html', {'cidades':cidades})
    def post(self, request):
        pass
class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'Curso.html', {'cursos':cursos})
    def post(self, request):
        pass
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'Disciplina.html', {'disciplinas':disciplinas})
    def post(self, request):
        pass
class DisciplinaporcursoView(View):
    def get(self, request, *args, **kwargs):
        disciplina_cursos = Disciplina_curso.objects.all()
        return render(request, 'Disciplina_curso.html', {'disciplina_cursos':disciplina_cursos})
    def post(self, request):
        pass
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencia = Frequencia.objects.all()
        return render(request, 'Frequencia.html', {'frequencia':frequencia})
    def post(self, request):
        pass
class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicao = Instituicao.objects.all()
        return render(request, 'Instituicao.html', {'instituicao':instituicao})
    def post(self, request):
        pass
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'Matricula.html', {'matriculas':matriculas})
    def post(self, request):
        pass
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'Ocorrencia.html', {'ocorrencias':ocorrencias})
    def post(self, request):
        pass
class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'Ocupacao.html', {'ocupacao':ocupacao})
    def post(self, request):
        pass
class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all()
        return render(request, 'Periodo.html', {'periodos':periodos})
    def post(self, request):
        pass
class TipoavaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipoavaliacao = Tipoavaliacao.objects.all()
        return render(request, 'Tipoavaliacao.html', {'tipoavaliacao':tipoavaliacao})
    def post(self, request):
        pass
class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'Turma.html', {'turmas':turmas})
    def post(self, request):
        pass
