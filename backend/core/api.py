from .serializers import LockerSerializer
from .models import Locker
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#Get List of all Lockers
class LockerAPIView(generics.ListAPIView):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer    
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'state']  
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

