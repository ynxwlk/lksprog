from django.db import models
from django.utils import timezone
import time

class mt(models.Model):# 格式为ACCESS格式
    # bh     =  models.AutoField('编号',primary_key=True) # 编号  自编号,长整型,递增,无重复
	ljxh    =  models.CharField('临时建设许可证号',max_length = 50, null=True, blank=True)  # 临建许号  文本 50
	sqdw    =  models.CharField('申请单位', max_length = 50, null=True, blank=True)  # 申请单位  文本 50
	sgdw    =  models.CharField('施工单位 ',max_length = 50, default='自建')  # 施工单位  文本 50
	sgdd    =  models.CharField('施工地点 ',max_length = 50, null=True, blank=True)  # 施工地点  文本 50
	sgqsrq  =  models.DateField('施工起始日期')    #, max_length = 20,default='2018年1月1日', null=True, blank=True)  # 施工起始日期    日期/时间
	sgzzrq  =  models.DateField('施工终止日期')    #, max_length = 20,default='2018年1月1日', null=True, blank=True)  # 施工终止日期    日期/时间
	syqsrq  =  models.DateField('证件有效期起始日期')    #, max_length = 20,default='2018年1月1日', null=True, blank=True)  # 使用起始日期    日期/时间
	syzzrq  =  models.DateField('证件有效期终止日期')    #, max_length = 20,default='2018年1月1日', null=True, blank=True)  # 使用终止日期    日期/时间
	gcnr    =  models.CharField('工程内容',max_length = 50, default='门头装修')  # 工程内容  文本 50
	gcmc    =  models.CharField('工程名称',max_length = 50, default='门头装修')  # 工程名称  文本 50
	mj      =  models.FloatField('面积')    #, max_digits=5， decimal_places=2)  # 建筑面积   浮点 50
	cd      =  models.FloatField('宽度')    #, max_digits=4， decimal_places=2)  # 宽度       浮点 50
	kd      =  models.FloatField('长度')    #, max_digits=4， decimal_places=2)  # 长度       浮点 50
	dong    =  models.CharField('东  ',max_length = 50, null=True, blank=True)  # 东  文本 50
	nan     =  models.CharField('南  ',max_length = 50, null=True, blank=True)  # 南  文本 50
	xi      =  models.CharField('西  ',max_length = 50, null=True, blank=True)  # 西  文本 50
	bei     =  models.CharField('北  ',max_length = 50, null=True, blank=True)  # 北  文本 50
	isPrint =  models.BooleanField('打印',default=False)  # 是否打印  文本 2
	sbrq    =  models.DateTimeField('申报日期', default = timezone.now)                 # 申报日期    日期/时间
	bzrq    =  models.DateTimeField('办证日期')   # null=True, blank=True)                  # 办证日期    日期/时间


	class Meta:
		ordering = ("-sbrq",)

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.sqdw
