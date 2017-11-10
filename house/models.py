# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Caiji (models.Model):
    chengshi = models.CharField('城市',max_length=200)
    qu = models.CharField('区',max_length=200)
    pian = models.CharField('片',max_length=200)
    xiaoqu = models.CharField('小区',max_length=200)
    huxing = models.CharField('户型',max_length=200)
    mianji = models.CharField('面积',max_length=200)
    danjia = models.CharField('单价',max_length=200)
    chaoxiang = models.CharField('朝向',max_length=200)
    louceng = models.CharField('楼层',max_length=200)
    zonglouceng = models.CharField('总楼层',max_length=200)
    zhuangxiu = models.CharField('装修',max_length=200)
    xuexiao = models.CharField('学校',max_length=200)
    niandai = models.CharField('建筑年代',max_length=200)
    dianti = models.CharField('有无电梯',max_length=200)
    chanquan = models.CharField('产权性质',max_length=200)

    zhuzhaileibie = models.CharField('住宅类别',max_length=200)
    jianzhujiegou = models.CharField('建筑结构',max_length=200)
    jianzhuleibie = models.CharField('建筑类别',max_length=200)
    jianzhuxingshi = models.CharField('建筑形式',max_length=200)

    guapai = models.CharField('挂牌时间',max_length=200)
    gengxin = models.CharField('最后更新',max_length=200)
    junjia = models.CharField('参考均价',max_length=200)
    leixing = models.CharField('物业类型',max_length=200)
    wuyefei = models.CharField('物业费用',max_length=200)
    jianzhu = models.CharField('建筑类型',max_length=200)
    nianxian = models.CharField('产权年限',max_length=200)
    lvhua = models.CharField('绿化率',max_length=200)
    rongji = models.CharField('容积率',max_length=200)
    fenliu = models.CharField('人车分流',max_length=200)
    loudong = models.CharField('总楼栋数',max_length=200)
    hushu = models.CharField('总户数',max_length=200)
    laiyuan = models.CharField('来源',max_length=200)
    zhiwen = models.CharField('数据指纹',max_length=200)
    create_date = models.DateTimeField('添加时间',auto_now_add=True)
    url = models.CharField('采集地址',max_length=200)
    status = models.CharField('状态',max_length=200)

    def __str__(self):
        return '{0}\t{1}\t{2}\t{3}'.\
        format(self.xiaoqu,self.huxing,self.mianji,self.danjia)

class Province (models.Model):
    name = models.CharField('名称',max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True,default=0.0)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class Qu(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class Pian(models.Model):
    qu = models.ForeignKey(Qu)
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class Xiaoqu(models.Model):
    pian = models.ForeignKey(Pian)
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class Xuexiao(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class Huxing(models.Model):
    name = models.CharField('名称',max_length=200)
    shi= models.IntegerField('室')
    ting = models.IntegerField('厅')
    wei = models.IntegerField('卫')
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class City_huxing(models.Model):
    city = models.ForeignKey(City)
    huxing = models.ForeignKey(Huxing)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return '{0}\t{1}\t{2}'. \
            format(self.city,self.huxing,self.danjia)

class Chaoxiang(models.Model):
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class City_chaoxiang(models.Model):
    city = models.ForeignKey(City)
    chaoxiang = models.ForeignKey(Chaoxiang)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return '{0}\t{1}\t{2}'. \
            format(self.city,self.chaoxiang,self.danjia)

class Louceng(models.Model):
    name = models.CharField('名称',max_length=200)
    lou = models.CharField('所在楼层',max_length=200)
    min = models.IntegerField('最小总楼层')
    max = models.IntegerField('最大总楼层')
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class City_louceng(models.Model):
    city = models.ForeignKey(City)
    louceng = models.ForeignKey(Louceng)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return '{0}\t{1}\t{2}'. \
            format(self.city,self.louceng,self.danjia)

class Chanquan(models.Model):
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class City_chanquan(models.Model):
    city = models.ForeignKey(City)
    chanquan = models.ForeignKey(Chanquan)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return '{0}\t{1}\t{2}'. \
            format(self.city,self.chanquan,self.danjia)

class Jianzhu(models.Model):
    name = models.CharField('名称',max_length=200)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return self.name

class City_jianzhu(models.Model):
    city = models.ForeignKey(City)
    jianzhu = models.ForeignKey(Jianzhu)
    danjia = models.FloatField('单价',null=True)
    xishu = models.FloatField('系数',null=True,default=1.0)

    def __str__(self):
        return '{0}\t{1}\t{2}'. \
            format(self.city,self.jianzhu,self.danjia)


class Fangwu(models.Model):

    city = models.ForeignKey(City)
    qu = models.ForeignKey(Qu)
    pian = models.ForeignKey(Pian)
    xiaoqu = models.ForeignKey(Xiaoqu)
    huxing = models.ForeignKey(Huxing)
    mianji = models.FloatField('面积')
    danjia = models.FloatField('单价')
    chaoxiang = models.ForeignKey(Chaoxiang)
    louceng = models.ForeignKey(Louceng)
    niandai = models.IntegerField('建筑年代')
    chanquan = models.ForeignKey(Chanquan)
    guapai = models.DateField('挂牌日期')
    gengxin = models.DateField('更新日期')
    jianzhu = models.ForeignKey(Jianzhu)
    zhiwen = models.CharField('数据指纹',max_length=200)

    def __str__(self):
        return '{0}\t{1}\t{2}\t{3}'. \
            format(self.xiaoqu,self.huxing,self.mianji,self.danjia)

