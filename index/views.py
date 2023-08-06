from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import serializers
from django.utils.datastructures import MultiValueDictKeyError
import pandas as pd
import random


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
                label_list = [0, 1, 2, 3, 4]
                posinega_list = [0, 1]
                dict1 = [[] for _ in range(len(label_list))]
                dict2 = []
                dict3 = []
                for i in range(len(df['text'])):
                    dict1[random.choice(label_list)].append(
                        df['text'][i]
                    )
                    dict2.append(
                        {
                            'text': df['text'][i],
                            'label': random.choice(label_list),
                            'posi-nega': random.choice(posinega_list)
                        }
                    )
                for i in range(len(label_list)):
                    dict3.append(
                        {
                            'label': i,
                            'summary': random.choice(dict1[i])
                        }
                    )
                response = {
                    'setting': dict3,
                    'data': dict2
                }
                return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
            else:
                return JsonResponse({'msg': 'please input csv file'})
        except MultiValueDictKeyError:
            return JsonResponse({'msg': 'bad'})
