from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
     """docstring"""
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
