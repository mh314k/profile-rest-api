from rest_framework import serializers

class heloserializer(serializers.Serializer):
    '''docstring'''
    name = serializers.CharField(max_length=10)
