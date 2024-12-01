from django.contrib import admin
from django.urls import path, include  # include para adicionar urls de outros apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),  # Adicionando URLs do app produtos
]
