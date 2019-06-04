from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from . import models
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


class HelloViewSet(viewsets.ViewSet):
    '''docstring'''

    def list(self, request):
        '''docstring'''
        a_viewset =[
            'm',
            'h',
            '3',
            '1',
            '4',
            'k',
        ]
        return Response({"message":"hello view sets", 'a_viewset':a_viewset})
    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
