from django.contrib.auth.backends import ModelBackend
from .models import User

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class EmailBackend(BaseBackend):
    """
    Custom backend de autenticação que permite login com email e senha.
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()  # Obtém o modelo de usuário customizado
        try:
            # Busca o usuário com base no email fornecido
            user = User.objects.get(email=email)
            
            # Verifica se a senha fornecida corresponde à senha do usuário
            if user and check_password(password, user.password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            # Tenta recuperar o usuário pelo UUID (chave primária)
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
