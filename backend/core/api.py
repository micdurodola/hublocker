from .serializers import LockerSerializer
from .models import Locker
from rest_framework import viewsets, generics, permissions


#Get List of all Lockers
class LockerAPIView(generics.ListAPIView):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = (permissions.AllowAny,)

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

