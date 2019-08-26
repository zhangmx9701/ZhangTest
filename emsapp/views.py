import uuid,os
from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from emsapp.models import Ems


def emsdefault(ems):
    return {'id': ems.id, 'name': ems.name, 'age': ems.age, 'salary': ems.salary, 'headpic': str(ems.headpic)}


def main(request):
    emslist = list(Ems.objects.all())
    return JsonResponse({'ems':emslist},safe=False,json_dumps_params={'default':emsdefault})


def addstatus(request):
    try:
        name = request.POST.get("name")
        salary = request.POST.get("salary")
        age = request.POST.get("age")
        headpic = request.FILES.get("headpic")
        if headpic:
            ext = os.path.splitext(headpic.name)
            headpic.name = str(uuid.uuid4()) + ext[1]
        with transaction.atomic():
            Ems.objects.create(name=name, age=age, salary=salary, headpic=headpic)
            return HttpResponse(1)
    except:
        return HttpResponse(0)



def update(request):
    id = request.GET.get("id")
    ems = Ems.objects.get(id=id)
    if ems:
        request.session["updateId"] = id
        return HttpResponse(1)
    return HttpResponse(0)


def loadupdate(request):
    param = request.GET.get("param")
    id = request.session.get(param)
    ems = Ems.objects.get(id=id)
    return JsonResponse({'eu':ems},safe=False,json_dumps_params={'default':emsdefault})


def updatestatus(request):
    try:
        with transaction.atomic():
            id = request.POST.get("eId")
            ems = Ems.objects.get(id=id)
            ems.name = request.POST.get("name")
            ems.salary = request.POST.get("salary")
            ems.age = request.POST.get("age")
            headpic = request.FILES.get("headpic")
            if headpic:
                ext = os.path.splitext(headpic.name)
                headpic.name = str(uuid.uuid4()) + ext[1]
                ems.headpic = headpic
            ems.save()
            return  HttpResponse(1)
    except:
        return HttpResponse(0)


def delete(request):
    id = request.GET.get("id")
    print(id)
    emp = Ems.objects.get(id=id)
    if emp:
        emp.delete()
        return HttpResponse(1)


def forcelogin(request):
    status =  request.session.get("login")
    if status == '200':
        return HttpResponse(1)
    return HttpResponse(0)
