from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),  # Incluindo as URLs do seu app
    path('', include('app.urls')),  # Define a rota para a página principal
]
