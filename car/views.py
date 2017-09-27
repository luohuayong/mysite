# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Province,City,Brand,Car,Model

import datetime

# Create your views here.


def index(request):
    province_list = Province.objects.order_by('id')
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    context = {'province_list': province_list}
    return render(request, 'car/index.html', context)

def price(request):
    return render(request,'car/price.html')


def result(request):
    city_name = request.POST['city']
    year = float(request.POST['year'])
    month = float(request.POST['month'])
    model_name = request.POST['model']
    xingshi = float(request.POST['xingshi'])

    city = City.objects.filter(name=city_name)[0]
    model = Model.objects.filter(name=model_name)[0]
    now = datetime.datetime.now()
    used_months = abs((now.year - year) * 12 + (now.month - month) * 1)
    w = [-0.00107872, -0.00319275, -0.08732923, -0.017029, 0.52155691]
    b = 0.00614169
    y = w[0] * model.id/10000.00 + \
        w[1] * city.id/1000.00 + \
        w[2] * used_months/1000.00 + \
        w[3] * xingshi/100.00 + \
        w[4] * float(model.price_new)/1000.00 + b
    # return render("评估价格：{0}万元".format(y*1000.00))
    return HttpResponse("评估价格：{0:.2f}万元".format(y*1000.00))

