# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import hashlib

# Create your models here.


class Province(models.Model):
    name = models.CharField("名称",max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField("名称",max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField("名称",max_length=200)
    first = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField("名称",max_length=200)
    type = models.CharField("类型",max_length=10,
                            choices=(('two', u"两厢"), ('three', u"三厢"), ('sport', u"跑车"), ('suv', u"SUV"),
                             ('mpv', u"MPV"), ('pickup', u"皮卡"), ('van', u"面包车"), ('other', u"其他")))

    def __str__(self):
        return self.name

class Model(models.Model):
    car = models.ForeignKey(Car)
    name = models.CharField("名称",max_length=200)
    price_new = models.DecimalField("新车指导价(万元)",max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Sale(models.Model):
    model = models.ForeignKey(Model)
    shangpai_date = models.DateTimeField("上牌时间",max_length=200)
    address = models.ForeignKey(City)
    xingshi = models.DecimalField("行驶里程(万公里)",max_digits=5,decimal_places=2)
    price = models.DecimalField("标价(万元)",max_digits=5,decimal_places=2)

    def __str__(self):
        return self.model

class RawData(models.Model):
    def create_guid(self):
        str=self.model_name + self.shangpai_date + \
            self.xingshi + self.price + self.address
        return hashlib.md5(str.encode('utf-8')).hexdigest()

    brand_name = models.CharField("品牌",max_length=200)
    brand_first = models.CharField("品牌首字母",max_length=200)
    car_name = models.CharField("车系",max_length=200)
    car_type = models.CharField("类型",max_length=200)
    model_name = models.CharField("型号",max_length=200)
    url = models.CharField("采集地址",max_length=200)
    shangpai_date = models.CharField("上牌时间",max_length=200)
    address = models.CharField("上牌城市",max_length=200)
    xingshi = models.CharField("行驶里程(万公里)",max_length=200)
    price = models.CharField("标价",max_length=200)
    price_new = models.CharField("新车指导价",max_length=200)
    website = models.CharField("来源网站",
                               choices=(('guzi','瓜子网'),('xin','优信')),max_length=200)
    guid = models.CharField("唯一码",max_length=200)

    def __str__(self):
        return self.model_name







