from django.contrib.auth.models import User
from cards.models import Card

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['owner', 'card_name']


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(source='card_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'card']
