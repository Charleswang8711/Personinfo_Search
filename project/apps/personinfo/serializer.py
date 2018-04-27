from rest_framework import serializers
from .models import PersonProfile
class PersonInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonProfile
        fields = '__all__'
