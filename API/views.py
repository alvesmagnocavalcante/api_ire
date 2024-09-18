from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.
class CenterViewSet(viewsets.ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

# CREAR CLASE VIEWSET POR MODELO E IMPORTARLO DESDE .SERIALIZER

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BetsViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetsSerializer

class WinnersViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnersSerializer

class LimitsViewSet(viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitsSerializer

class ClasifiedViewSet(viewsets.ModelViewSet):
    queryset = Clasified.objects.all()
    serializer_class = ClasifiedSerializer

class CheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = CheduleSerializer

class ThrowViewSet(viewsets.ModelViewSet):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlansSerializer