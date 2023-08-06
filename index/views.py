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

                # declare tokenize
                def tokenize(text):
                    tokenizer = Tokenizer()
                    tokens = tokenizer.tokenize(text)
                    return [token.surface for token in tokens]

                # tokenize
                try:
                    tokenized_texts = [tokenize(text) for text in df['text']]
                except MultiValueDictKeyError:
                    return JsonResponse({'msg': 'csv file format is invalid'})

                return JsonResponse({'msg': 'nice'})
            else:
                return JsonResponse({'msg': 'please input csv file'})
        except MultiValueDictKeyError:
            return JsonResponse({'msg': 'bad'})
