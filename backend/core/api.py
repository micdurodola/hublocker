from .serializers import LockerSerializer
from .models import Locker
from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend


#Get List of all Lockers
class LockerAPIView(generics.ListAPIView):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'state']

#Locker Detail View
class LockerDetailAPIView(generics.RetrieveAPIView):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = (permissions.AllowAny,)

#Post a Locker
class LockerCreateAPIView(generics.ListCreateAPIView): 
    queryset = Locker.objects.all()   
    serializer_class = LockerSerializer
    permission_classes = (permissions.AllowAny,)

