from django.contrib import admin
from django.urls import path 
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('Cidade/', CidadeView.as_view(), name="Cidade"),
    path('Pessoa/', PessoaView.as_view(), name = 'Pessoa'),
    path('Areasaber/', AreasaberView.as_view(),name='Areasaber'),
    path('Avaliacao/', AvaliacaoView.as_view(),name='Avaliacao'),
    path('Curso/', CursoView.as_view(),name='Curso'),
    path('Disciplina/', DisciplinaView.as_view(), name='Disciplina'),
    path('Disciplina_curso/', DisciplinaporcursoView.as_view(),name='Disciplina_curso'),
    path('Frequencia/', FrequenciaView.as_view(),name='Frequencia'),
    path('Instituicao/', InstituicaoView.as_view(),name='Instituicxao'),
    path('Matricula/', MatriculaView.as_view(),name='Matricula'),
    path('Ocorrencia/', OcorrenciaView.as_view(), name='Ocorrencia'),
    path('Ocupacao/', OcupacaoView.as_view(),name='Ocupacao'),
    path('Periodo/', PeriodoView.as_view(),name='Periodo'),
    path('Tipoavaliacao/', TipoavaliacaoView.as_view(), name='Tipoavaliacao'),
    path('Turma/', TurmaView.as_view(),name='Turma'),
    ]