from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import serializers
from django.utils.datastructures import MultiValueDictKeyError
import pandas as pd
from janome.tokenizer import Tokenizer


# Create your views here.
class IndexView(viewsets.ViewSet):
    serializer_class = serializers.IndexSerializer

    def get_response(self, request):
        return JsonResponse({'msg': 'please post'})

    def post_response(self, request):
        try:
            input_file = request.FILES['input_file']
            if input_file.content_type == 'text/csv':
                df = pd.read_csv(input_file)
                return JsonResponse({'msg': df['text'].tolist()}, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'msg': 'please input csv file'})
        except MultiValueDictKeyError:
            return JsonResponse({'msg': 'bad'})
