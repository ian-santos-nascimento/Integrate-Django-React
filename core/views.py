from django.shortcuts import render
from .Serializers import ListSerializer,ItemSerializer
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .models import List,Item
# Create your views here.


class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    #Metodo pra filtar resultado por usuario
    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)

class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
        permission_classes = [permissions.IsAuthenticated]
        authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]