# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
import time
from django.utils import timezone
 
from mt.models import mt
 
# 数据库操作
def mtdb(request):
    mt1 = mt(ljxh='临建许号',\
     sqdw ='申请单位',\
     #  sgdw='自建',\
     sgdd = '施工地点', \
     sgqsrq = date(),\
     sgzzrq = date(),\
     syqsrq = date(),\
     syzzrq = date(),\
     gcdd  = '工程地点',\
     gcmc  = '工程名称',\
     jzmj  = '建筑面积',\
     cd    = '长度',\
     kd    = '宽度',\
     dong  = '东',\
     nan   = '南',\
     xi    = '西',\
     bei   = '北')
     # dayin = True)
    #      bzrq =date() )  #sbrq  = date(),
    mt1.save()
    return HttpResponse("<p>数据添加成功！</p>")
