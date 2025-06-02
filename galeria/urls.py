from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
        path('', index, name='indexUrl'),
        path('imagem/', imagem, name='imagemUrl'),
]