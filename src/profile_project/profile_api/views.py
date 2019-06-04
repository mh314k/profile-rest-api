from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.
class HelloApiView(APIView):
     """docstring"""
     serializer_class = serializers.heloserializer

     def get(self, request, format=None):
         '''docstring'''
         an_api = [
            'محمد',
            'حسین',
            'خانی',
            'کوثر',
            'خیزی'
         ]
         return Response({'message':"hello",
            'an_api':an_api
         })
     def post(self, request):
        '''docstring'''
        serializer = serializers.heloserializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method': 'put'})

     def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method': 'patch'})

     def delete(self, request, pk=None):
        """Deletes and object."""

        return Response({'method': 'delete'})
