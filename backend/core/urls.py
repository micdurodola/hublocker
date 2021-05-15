from django.urls import path
from .api import LockerAPIView,LockerCreateAPIView,LockerDetailAPIView

urlpatterns = [
    path('',LockerAPIView.as_view()),
    path('<int:pk>/',LockerAPIView.as_view()),
    path('add/',LockerCreateAPIView.as_view()),
    
]