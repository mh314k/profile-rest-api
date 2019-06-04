from rest_framework import serializers

from .models import UserProfile

class heloserializer(serializers.Serializer):
    '''docstring'''
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """doc"""
    class Meta:
        model=UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = UserProfile(email=validated_data['email'],
            name= validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
