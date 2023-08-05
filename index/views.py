from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import serializers


# Create your views here.
class IndexView(viewsets.ViewSet):
    serializer_class = serializers.IndexSerializer

    def index(self, request):
        return JsonResponse({'msg': 'render_test'})