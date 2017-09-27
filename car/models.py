# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import hashlib

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    first = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10,
                            choices=(('two', u"两厢"), ('three', u"三厢"), ('sport', u"跑车"), ('suv', u"SUV"),
                             ('mpv', u"MPV"), ('pickup', u"皮卡"), ('van', u"面包车"), ('other', u"其他")))

    def __str__(self):
        return self.name

class Model(models.Model):
    car = models.ForeignKey(Car)
    name = models.CharField(max_length=200)
    price_new = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Sale(models.Model):
    model = models.ForeignKey(Model)
    shangpai_date = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    xingshi = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.model

class RawData(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_first = models.CharField(max_length=200)
    car_name = models.CharField(max_length=200)
    car_type = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    shangpai_date = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    xingshi = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    price_new = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    guid = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name

    def create_guid(self):
        str=self.model_name + self.shangpai_date + \
            self.xingshi + self.price + self.address
        return hashlib.md5(str.encode('utf-8')).hexdigest()





