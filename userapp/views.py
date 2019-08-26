import random,string,os,uuid

import django
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from userapp.captcha.image import ImageCaptcha
from userapp.models import User


def registlogic(request):
    username = request.POST.get("username")
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    sex = request.POST.get("sex")
    headpic = request.FILES.get("headpic")
    try:
        if headpic:
            ext = os.path.splitext(headpic.name)
            headpic.name = str(uuid.uuid4()) + ext[1]
        User.objects.create(username=username,
                                  name=name,
                                  pwd=pwd,
                                  sex=sex,
                                  headpic=headpic)
        return HttpResponse(1)

    except:
        return HttpResponse(0)


def login(request):
    name = request.COOKIES.get("username")
    pwd = request.COOKIES.get("userpwd")
    res = User.objects.filter(username=name,pwd=pwd)
    if res:
        request.session["login"]="200"
        return HttpResponse(1)
    return HttpResponse(0)


def loginlogic(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    rem = request.POST.get("remember")
    res = User.objects.filter(username=name,pwd=pwd)
    if res:
        response = HttpResponse(1)
        if rem:
            response.set_cookie("username", name, max_age=7 * 24 * 3600)
            response.set_cookie("userpwd", pwd, max_age=7 * 24 * 3600)
        request.session["login"] = "200"
        return response
    return  HttpResponse(0)

def getcaptcha(request):
    image = ImageCaptcha()
    image_codes = random.sample(string.ascii_letters + string.digits,4)
    image_codes = "".join(image_codes)
    request.session["codes"] = image_codes
    data = image.generate(image_codes)
    return HttpResponse(data,"image/png")

def usercheck(request):
    name = ''
    if request.method == "GET":
        name = request.GET.get("username")
    elif request.method == "POST":
        name = request.POST.get("username")
    user = User.objects.filter(username=name)
    if user:
        return HttpResponse(0)
    return HttpResponse(1)

def numcheck(request):
    num = ''
    if request.method == "GET":
        num = request.GET.get("num")
    elif request.method == "POST":
        num = request.POST.get("num")
    numSession = request.session.get("codes")
    if num.lower() == numSession.lower():
        return HttpResponse(1)
    else:
        return HttpResponse(0)