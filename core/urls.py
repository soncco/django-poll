from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('resultados/<int:id>', views.resultados, name='resultados'),
]
