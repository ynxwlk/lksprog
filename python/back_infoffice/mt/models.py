from django.db import models

class MengTouBiaoShi(models.Model):# 格式为ACCESS格式
    bh     =  models.AutoField('编号',primary_key=True) # 编号  自编号,长整型,递增,无重复
    ljxh   =  models.CharField('临时建设许可证号',max_length = 50)  # 临建许号  文本 50
    sqdw   =  models.CharField('申请单位', max_length = 50)  # 申请单位  文本 50
    sgdw   =  models.CharField('施工单位 ',max_length = 50)  # 施工单位  文本 50
    sgdd   =  models.CharField('施工地点 ',max_length = 50)  # 施工地点  文本 50
    sgqsrq =  models.DateField('施工起始日期 ')  # 施工起始日期    日期/时间
    sgzzrq =  models.DateField('施工终止日期 ')  # 施工终止日期    日期/时间
    syqsrq =  models.DateField('使用起始日期 ')  # 使用起始日期    日期/时间
    syzzrq =  models.DateField('使用终止日期 ')  # 使用终止日期    日期/时间
    # gcnr   =  models.CharField('工程内容',max_length = 50)  # 工程内容  文本 50
    gcdd   =  models.CharField('工程地点',max_length = 50)  # 工程地点  文本 50
    gcmc   =  models.CharField('工程名称',max_length = 50)  # 工程名称  文本 50
    # jg     =  models.CharField('结构',max_length = 50)  # 结构  文本 50
    # cs     =  models.CharField('层数',max_length = 50)  # 层数  文本 50
    # ds     =  models.CharField('幢数',max_length = 50)  # 幢数  文本 50
    jzmj   =  models.CharField('建筑面积',max_length = 50)  # 建筑面积  文本 50
    cd     =  models.CharField('宽度',max_length = 50)  # 宽度  文本 50
    kd     =  models.CharField('长度',max_length = 50)  # 长度  文本 50
    dong   =  models.CharField('东  ',max_length = 50)  # 东  文本 50
    nan    =  models.CharField('南  ',max_length = 50)  # 南  文本 50
    xi     =  models.CharField('西  ',max_length = 50)  # 西  文本 50
    bei    =  models.CharField('北  ',max_length = 50)  # 北  文本 50
    dayin    =  models.CharField('打印',max_length = 2)  # 是否打印  文本 2
    sbrq   =  models.DateField('申报日期')                  # 申报日期    日期/时间
    bzrq   =  models.DateField('办证日期')                  # 办证日期    日期/时间

    # def __str__(self):              # __unicode__ on Python 2
    #     return self.ljxk


