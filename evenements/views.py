from django.shortcuts import render
from evenements.models import Evenements
from evenements.serializers import EvenementsSerializer
from rest_framework.decorators import api_view ,authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.

#Afficher tous les evenements ordonnées par date 
@api_view(['GET'])
@permission_classes([AllowAny])
def evenementsList(request):
    events= Evenements.objects.all().order_by('date')
    serializer = EvenementsSerializer(events, many=True)
    return Response(serializer.data)

#Afficher le detail d'un evenement
@api_view(['GET'])
@permission_classes([AllowAny])
def DetailEvenement(request, id):
    events = Evenements.objects.get(id=id)
    serilizer = EvenementsSerializer(events, many=False)
    return Response(serilizer.data)

#les utilisateurs connectées peuvents ajouter des evenemnts
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser])
def AjouterEvenements(request):
    serializer = EvenementsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(utilisateur=request.user) 
        return Response(serializer.data)  
   
    return Response(serializer.errors)   


#l'utilisateur connecté peut modifier son evenements 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def eventsUpdate(request,pk):
    events = Evenements.objects.get(id=pk)
    serializer =EvenementsSerializer(instance=events,data=request.data)

    if serializer.is_valid():
        serializer.save(utilisateur=request.user)
        return Response(serializer.data)            
    return Response(serializer.errors)

#l'utilisatuer connecté peut supprimé son evenements 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteEvents(request,pk):
    events = Evenements.objects.get(id=pk)
    if request.user == events.utilisateur:
       
      events.delete()
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST) 