# coding: utf-8
from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse
from django.core import serializers
from django.http.response import JsonResponse
import csv
import json
import sys
import os
from django.conf import settings

file_ = open(os.path.join(settings.BASE_DIR, 'csv/sdvxdata.csv'), "r", encoding = "utf-8")

def show(request):
    res = {}
    json_listm = []

    with file_ as data:
        for line in csv.DictReader(data):
            json_listm.append(line)

    res["music_data"] = json_listm
    
    '''
    with open('../json/artistdata.json', 'w') as f:
        # JSONへの書き込み
        json.dump(json_lista, f)
    '''

    return JsonResponse(res)