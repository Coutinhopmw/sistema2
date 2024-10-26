import logging

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

logger = logging.getLogger('sistema2')

class Login(View):
    
    def get(self, request):
        contexto = { 'mensagem': ''}
        if not request.user.is_authenticated:
            return render(request, 'autenticacao.html', contexto) 
        else:
            return HttpResponse('usuário já está altenticado')
        
    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)
        
        logger.info('usuario:{}'.format(usuario))
        print(f'usuario: {usuario}')
        print(f'senha: {senha}')
        logger.info('senha:{}'.format(senha))

        user = authenticate(request, username = usuario, password = senha)
        print(f'user: {user}')

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponse('Usuário auticado com sucesso!')
            return render(request, 'autenticacao.html', {'mensagem' : 'Usuário inativo.' }) 
        return render(request, 'autenticacao.html', {'mensagem' : 'Usuário ou senha inválido.' })   


class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })