from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import serializers


# Create your views here.
class IndexView(viewsets.ViewSet):
    serializer_class = serializers.IndexSerializer

    def get_response(self, request):
        return JsonResponse({'msg': 'please post'})

    def post_response(self, request):
        return JsonResponse({'msg': 'nice'})
