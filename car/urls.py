#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Leo on 2017/9/22

"""
代码说明：
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'city/(\d+)', views.city, name='city'),
    url(r'car/(\d+)', views.car, name='car'),
    url(r'model/(\d+)', views.model, name='model'),
    url(r'^price$', views.price, name='price'),
    url(r'^result$', views.result, name='result'),
]

if __name__ == '__main__':
    pass