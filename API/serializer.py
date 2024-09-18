from rest_framework import serializers
from .models import *

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'

# CREAR CLASE SERIALIZER POR MODELO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'

class WinnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'

class LimitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = '__all__'

class ClasifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasified
        fields = '__all__'

class CheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ThrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Throw
        fields = '__all__'

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

