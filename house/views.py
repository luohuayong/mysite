# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Province,City,Qu,Pian,Xiaoqu,Huxing,Chaoxiang,Louceng,Jianzhu,Chanquan

import datetime

# Create your views here.


def index(request):
    province_list = Province.objects.order_by('id')
    huxing_list = Huxing.objects.order_by('id')
    chaoxiang_list = Chaoxiang.objects.order_by('id')
    louceng_list = Louceng.objects.order_by('id')
    jianzhu_list = Jianzhu.objects.order_by('id')
    chanquan_list = Chanquan.objects.order_by('id')

    context = {'province_list': province_list,
               'huxing_list': huxing_list,
               'chaoxiang_list': chaoxiang_list,
               'louceng_list': louceng_list,
               'jianzhu_list': jianzhu_list,
               'chanquan_list': chanquan_list}
    return render(request, 'house/index.html', context)

def city(request,id):
    city_list = City.objects.filter(province=id)
    list = []
    for item in city_list:
        list.append({'id':item.id,'name':item.name})
    print(list)
    return JsonResponse({'data':list})

def qu(request,id):
    qu_list = Qu.objects.filter(city=id)
    list = []
    for item in qu_list:
        list.append({'id':item.id,'name':item.name})
    print(list)
    return JsonResponse({'data':list})

def pian(request,id):
    pian_list = Pian.objects.filter(qu=id)
    list = []
    for item in pian_list:
        list.append({'id':item.id,'name':item.name})
    print(list)
    return JsonResponse({'data':list})

def xiaoqu(request,id):
    xiaoqu_list = Xiaoqu.objects.filter(pian=id)
    list = []
    for item in xiaoqu_list:
        list.append({'id':item.id,'name':item.name})
    print(list)
    return JsonResponse({'data':list})

def result(request):
    xiaoqu = request.POST['xiaoqu']
    huxing = request.POST['huxing']
    chaoxiang = request.POST['chaoxiang']
    louceng = request.POST['louceng']
    chanquan = request.POST['chanquan']
    jianzhu = request.POST['jianzhu']
    mianji = request.POST['mianji']
    niandai = request.POST['niandai']


    str = '小区：{0}\n户型：{1}\n朝向：{2}\n楼层：{3}\n产权：{4}\n类型：{5}\n面积：{6}\n年代：{7}'.\
        format(xiaoqu,huxing,chaoxiang,louceng,chanquan,jianzhu,mianji,niandai)

    return HttpResponse(str)

