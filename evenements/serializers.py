from accounts.serializers import UserSerializer
from evenements.models import Evenements
from rest_framework import serializers

class EvenementsSerializer(serializers.ModelSerializer):
    utilisateur=UserSerializer(read_only=True)
 
    class Meta:
        model = Evenements
        fields ='__all__'
      
        depth = 1