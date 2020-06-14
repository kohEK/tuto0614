from django.contrib.auth.models import User
from rest_framework import viewsets, request
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from cards.models import Card
from cards.serializers import UserSerializer, CardSerializer


class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data('username'))
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user_id': user.pk, 'token': token.key})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
