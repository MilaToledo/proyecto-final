from django.urls import path
from AppCoder.views import *


urlpatterns = [
        path('inicio/', view_inicio),
        path('cursos/', view_cursos)
]
