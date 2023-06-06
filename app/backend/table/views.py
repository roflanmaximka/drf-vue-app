from django.http import JsonResponse
from django.shortcuts import render

from .models import Record


# Create your views here.

def index(request):
    records = []

    for record in Record.objects.all():
        records.append({
            'employee_name':record.employee_name,
            'raw_material_name': record.raw_material_name,
            'iron_concentration': record. iron_concentration,
            'silicon_concentration':record.silicon_concentration,
            'aluminum_concentration': record.aluminum_concentration,
            'calcium_concentration': record.calcium_concentration,
            'sulfur_concentration': record.sulfur_concentration,
            'created_at': record.created_at
        })

    return JsonResponse(records, safe=False)