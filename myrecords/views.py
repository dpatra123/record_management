from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myrecords.models import *
import os, ast, json, subprocess
from django.core.files.storage import FileSystemStorage
import re

def myRecords(request):
    my_records = Records.objects.all()
    my_response = {}
    for x in my_records:
        my_response[x] = x.__dict__
    return render(request, "my_records.html",{"my_response":my_response})

def myDashboard(request):
    return render(request, "dashboard.html",{"name":'My Records', "title": 'My Govt files'})

def manageRecords(request):
    return render(request, "manage_records.html",{"name":'My Records', "title": 'My Govt files'})

def addRecord(request):
    states = State.objects.values_list('state_name',flat=True)
    state_dist_map = {}
    inst_type_name_map = {}
    case_type_map = {}
    for s in states:
        dist = District.objects.filter(state__state_name=s).values_list('dist_name', flat=True)
        state_dist_map[s] = list(dist)
    inst_types = InstitutionType.objects.values_list('institution_type',flat=True)
    for itype in inst_types:
        inst_name = InstitutionName.objects.filter(institution_type__institution_type=itype).values_list('institution_name', flat=True)
        inst_type_name_map[itype] = list(inst_name)
    case_types = CaseType.objects.values_list('case_type',flat=True)
    return render(request, "add_record.html",{"sdmap":ast.literal_eval(json.dumps(state_dist_map)), "itnmap": ast.literal_eval(json.dumps(inst_type_name_map)), "casetypes":case_types})

def saveRecord(request):
    recordName = request.POST.get('recordName')
    state = request.POST.get('state')
    dist = request.POST.get('dist')
    institution_type = request.POST.get('institution_type')
    institution_name = request.POST.get('institution_name')
    petitioner_name = request.POST.get('petitioner_name')
    case_type = request.POST.get('case_type')
    case_number = request.POST.get('case_number')
    file_number = request.POST.get('file_number')
    counter_filed = request.POST.get('counter_filed')
    cf_lr = request.POST.get('cf_lr')
    cf_dt = request.POST.get('cf_dt')
    date_of_order = request.POST.get('date_of_order')
    memorandum_sought = request.POST.get('memorandum_sought')
    ms_lr = request.POST.get('ms_lr')
    ms_dt = request.POST.get('ms_dt')
    memorandum_received = request.POST.get('memorandum_received')
    mr_lr = request.POST.get('mr_lr')
    mr_dt = request.POST.get('mr_dt')
    status_of_comp = request.POST.get('status_of_comp')
    sc_lr = request.POST.get('sc_lr')
    sc_dt = request.POST.get('sc_dt')
    fao_filed = request.POST.get('fao_filed')
    fao_lr = request.POST.get('fao_lr')
    fao_dt = request.POST.get('fao_dt')
    try:
        record = Records(record_name = recordName, state = state, dist = dist, institution_type = institution_type, institution_name = institution_name,
                     petitioner_name = petitioner_name, case_type = case_type, case_number = case_number, file_number = file_number,
                     counter_filed = counter_filed, cf_lr = cf_lr, cf_dt = cf_dt, date_of_order = date_of_order, memorandum_sought = memorandum_sought,
                     ms_lr = ms_lr, ms_dt = ms_dt, memorandum_received = memorandum_received, mr_lr = mr_lr, mr_dt = mr_dt,
                     status_of_comp = status_of_comp, sc_lr = sc_lr, sc_dt = sc_dt, fao_filed = fao_filed, fao_lr = fao_lr, fao_dt = fao_dt)
        record.save()
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
# Create your views here.
