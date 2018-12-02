from django.db import models
from django.utils import timezone


# Create your models here.
# class JianSheDanWei(models.Model):            #建设单位
#     BianHao                 = models.AutoField(primary_key=True)    #编号
#     Name                    = models.CharField('建设单位',max_length=128)      #建设单位
#     DiZhi                   = models.CharField('建设单位住址',max_length=128)      #建设单位住址
#     FaDingDaiBiaoRen        = models.CharField('法定代表人',max_length=8)        #法定代表人
#     FaDingDaiBiaoRenDianHua = models.CharField('法定代表人联系电话',max_length=11)       #法定代表人联系电话
#     LianXiRen               = models.CharField('联系人',max_length=8)        #联系人
#     LianXiRenDianHua        = models.CharField('联系人电话',max_length=11)       #联系人电话
#     DianHua                 = models.CharField('建设单位电话',max_length=15)       #建设单位电话
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class FaGaiPiWen(models.Model):                             #发改批文
#     BianHao       = models.AutoField( ' primary_key=True)    #编号
#     PiWen         = models.CharField( '发改部门文件', max_length=50)       #发改部门文件
#     FaWenRiQi     = models.DateField( '发改部门发文日期', )                    #发改部门发文日期
#     YongDiMianJi  = models.FloatField('发改部门文件用地面积',)                     #发改部门文件用地面积
#     JianSheGuiMo  = models.CharField( '发改部门文件建筑规模',max_length=50)        #发改部门文件建筑规模
#     JianZhuMianJi = models.FloatField('发改批文建筑面积', )                    #发改批文建筑面积
#     TouZi         = models.FloatField('发改部门文件投资', )                    #发改部门文件投资
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class XuanZhiYiJianShu(models.Model):      #选址意见书
#     BianHao      = models.CharField(max_length=50)    #选址意见书编号
#     BanZhengRiQi = models.DateField()     #选址意见书发证日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class GuoTuZhengJian(models.Model):        #土地使用证
#     BianHao                               = models.AutoField(primary_key=True)    #编号
#     WenJian         = models.CharField(max_length=50)    #土地部门文件
#     FaWengRiQi      = models.DateField()    #土地部门文件批准日期
#     TuDiZhengHao         = models.CharField(max_length=50)    #土地使用证号
#     TuDiBanZhengRiQi    = models.DateField()    #土地部门发证日期
#     YongDiMianJi    = models.FloatField()    #土地证用地面积
#     YongDixinzhi    = models.CharField(max_length=50)    #土地证用地性质
#     ZongDiTuBianHao = models.CharField(max_length=50)    #宗地图编号
#     HeTong          = models.CharField(max_length=50)    #土地出让合同
#     BeiZhu          = models.TextField()    #土地证备注
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class GuiHuaTiaoJian(models.Model):   #规划条件
#     BianHao      = models.CharField(max_length=50)    #规划设计条件编号
#     PiZhunRiQi   = models.DateField()    #规划设计条件批准日期
#     WeiZhi       = models.CharField(max_length=50)    #规划设计条件地块位置
#     YongDiMianJi = models.FloatField()    #规划设计条件用地面积
#     YongDixinzhi = models.CharField(max_length=50)    #规划设计条件用地性质
#     RongJiLu     = models.FloatField()    #规划设计条件容积率
#     JianZhuMiDu  = models.FloatField()    #规划设计条件建筑密度
#     LuDiLu       = models.FloatField()    #规划设计条件绿地率
#     BeiZhu       = models.TextField()    #规划设计条件备注
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class GuiHuaFangAn(models.Model):           #规划方案
#     BianHao          = models.CharField(max_length=50)    #批准的平面规划图编号
#     PiZhunRiQi       = models.DateField()    #规划方案批准日期
#     YongDiMianJi     = models.FloatField()    #规划方案用地面积
#     JianZhuMianJi    = models.FloatField()    #规划方案建筑面积
#     JiRongMianJi     = models.FloatField()    #规划方案计容面积
#     ZhuZeMianJi      = models.FloatField()    #规划方案住宅面积
#     GongJianMianJi   = models.FloatField()    #规划方案公建面积
#     ShangYeMianJi    = models.FloatField()    #规划方案商用面积
#     FeiJiRongMianJi  = models.FloatField()    #规划方案不计容面积
#     DiXiaMianJi      = models.FloatField()    #规划方案地下层面积
#     JiaKongCenMianJi = models.FloatField()    #规划方案架空层面积
#     RongJiLu         = models.FloatField()    #规划方案容积率
#     ZhanDiMianJi     = models.FloatField()    #规划方案建筑基底面积
#     JianZhuMiDu      = models.FloatField()    #规划方案建筑密度
#     LuDiMianJi       = models.FloatField()    #规划方案绿地面积
#     LuDiLu           = models.FloatField()    #规划方案绿地率
#     TingCheWei       = models.FloatField()    #规划方案停车位
#     BeiZhu           = models.TextField()    #规划方案备注
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class YongDiGuiHuaXuKe(models.Model):       #用地规划许可证
#     ZiBianHao      = models.CharField(max_length=50)    #用地规划许分局自编号
#     BaoJianRiQi    = models.DateField()    #用地规划许可报件日期
#     ShangBaoRiQi   = models.DateField()    #用地规划许可报件送市局日期
#     BeiZhu         = models.TextField()    #办理用地规划许可证备注
#     ShengChaYiJian = models.TextField()    #办理用地规划许可证初审意见
#     BianHao        = models.CharField(max_length=50)    #用地规划许可证编号
#     BanZhengRiQi   = models.DateField()    #用地规划许可证办证日期
#     YongDixinzhi   = models.CharField(max_length=50)    #用地规划许可证用地性质
#     YongDiMianJi   = models.FloatField()    #用地规划许可证用地面积
#     JianZhuMianJi  = models.FloatField()    #用地规划许可证建设规模
#     LinZhengRiQi   = models.DateField()    #用地规划许可证领证日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class ShiGongTu(models.Model):          #施工图
#     BianHao       = models.CharField(max_length=50)    #经图审的施工图
#     TuShengDanWei = models.CharField(max_length=50)  #设计单位
#     TuShengRiQi   = models.DateField()    #图审日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class LuHuaJingGuanFangAn(models.Model):      #绿化景观
#     BianHao       = models.CharField(max_length=50)    #绿化景观方案
#     ShengDingRiQi = models.DateField()    #绿化景观方案审定日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class KaiGongTongJiDengJiBiao(models.Model):     #固定资产投资项目新开工统计登记表
#     BianHao = models.CharField(max_length=50)    #固定资产投资项目新开工统计登记表
#     RiQi    = models.DateField()    #固定资产投资项目新开工统计登记表办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class BaoJianBiao(models.Model):          #工程建设项目报建表
#     BianHao = models.CharField(max_length=50)    #工程建设项目报建表
#     RiQi    = models.DateField()    #工程建设项目报建表办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class QiangGai(models.Model):        #墙改预缴款结算通知书
#     BianHao = models.CharField(max_length=50)    
#     RiQi    = models.DateField()    #墙改预缴款、结算通知书办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class RenFang(models.Model):             #人民防空建设许可
#     BianHao = models.CharField(max_length=50)    
#     RiQi    = models.DateField()    #人民防空建设许可办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class HuanJingYingXiang(models.Model):         #建设项目环境影响报告
    # BianHao = models.CharField(max_length=50)    
    # RiQi    = models.DateField()    #建设项目环境影响报告办理日期
    # def __str__(self):              # __unicode__ on Python 2
    #     return self.name


# class KangZheng(models.Model):     #抗震设防要求管理意见书
#     BianHao = models.CharField(max_length=50)    
#     RiQi    = models.DateField()    #抗震设防要求管理意见书办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class HuanWei(models.Model):            #环卫审核备案登记
#     BianHao = models.CharField(max_length=50)    #编号
#     RiQi    = models.DateField()    #环卫审核备案登记办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class DangAn(models.Model):        #报送建设工程档案责任书
#     BianHao = models.CharField(max_length=50)    #报送建设工程档案责任书
#     RiQi    = models.DateField()    #报送建设工程档案责任书办理日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class JianSheGongChengGuiHuaXuKe(models.Model):       #建设工程规划许可证
#     BianHao                               = models.AutoField(primary_key=True)    #编号
#     BaoJianRiQi   = models.DateField()    #建设工程规划许可报件日期
#     ZiBianHao     = models.CharField(max_length=50)    #建设工程规划许分局自编号
#     ShangBaoRiQi  = models.DateField()    #建设工程规划许可报件送市局日期
#     BeiZhu        = models.CharField(max_length=50)    #办理建设工程规划许可证备注
#     YiJian        = models.TextField()    #办理建设工程规划许可证初审意见
#     BianHao       = models.CharField(max_length=50)    #建设工程规划许编号
#     JianSheGuiMo  = models.TextField()    #建设工程规划许建设规模
#     JianZhuMianJi = models.FloatField()    #建设工程规划许建设面积
#     BeiZhu        = models.TextField()    #建设项目审批内容明细表
#     BanZhengRiQi  = models.DateField()    #建设工程规划许办证日期
#     LinZhengRiQi  = models.DateField()    #建设工程规划许可证领证日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class JunGongCeLiang(models.Model):            #竣工测量成果资料
#     BianHao      = models.CharField(max_length=50)    #竣工测量成果资料编号
#     RiQi         = models.DateField()    #竣工测量成果资料出图日期
#     YongDiMianJi = models.FloatField()    #竣工用地面积
#     ZhanDiMianJi = models.FloatField()    #竣测建筑占地面积
#     JianZhuMiDu  = models.FloatField()    #竣工建筑密度
#     LuDiMianJi   = models.FloatField()    #竣工绿地面积
#     LuDiLu       = models.FloatField()    #竣工绿地率
#     TingCheWei   = models.FloatField()    #竣工停车位
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class FangChanCeHui(models.Model):            #房产面积测绘报告书
#     BianHao          = models.CharField(max_length=50)    #房产面积测绘报告书编号
#     RiQi             = models.DateField()    #房产面积测绘报告书办理日期
#     diShangmiji      = models.FloatField()    #竣工地上建筑面积
#     JiRongMianJi     = models.FloatField()    #竣工计容面积
#     ZhuZeMianJi      = models.FloatField()    #竣工住宅面积
#     GongJianMianJi   = models.FloatField()    #竣工公建面积
#     ShangYeMianJi    = models.FloatField()    #竣工商用面积
#     FeiJiRongMianJi  = models.FloatField()    #竣工不计容面积
#     DiXiaMianJi      = models.FloatField()    #竣工地下层面积
#     JiaKongCenMianJi = models.FloatField()    #竣工架空层面积
#     RongJiLu         = models.FloatField()    #竣工容积率
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class GuiHuaYanShou(models.Model):         #规划验收合格证
#     BianHao                               = models.AutoField(primary_key=True)    #编号
#     BaoJianRiQi     = models.DateField()    #竣工验收报件日期
#     ZiBianHao       = models.CharField(max_length=50)    #竣工验收分局自编号
#     ShangBaoRiQi    = models.DateField()    #竣工验收报件送市局日期 
#     GenZongFuWuBiao = models.CharField(max_length=50)    #验线表或跟踪服务表
#     BeiZhu          = models.TextField()    #验收备注
#     YiJian          = models.TextField()    #竣工验收合格证初审意见
#     BianHao         = models.CharField(max_length=50)    #竣工验收合格证编号
#     BanZhengRiQi    = models.DateField()    #竣工验收合格证办证日期
#     LinZhengRiQi    = models.DateField()    #竣工验收合格证领证日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class ShouFeiBiaoZhun(models.Model):          #收费标准  未进入项目表
#     BianHao                               = models.AutoField(primary_key=True)    #编号
#     BaDiDingZhuang = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩收费标准
#     YanXian        = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费标准
#     JunGongCeLiang = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费标准
#     ZhuanJiaZiXun  = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费标准
#     DiTuCeHui      = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费收费标准
#     ZhuZe          = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅收费标准
#     FeiZhuZe       = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅收费标准
#     LinShiXiangMu  = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目收费标准
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class CeHuiShouFei(models.Model):            #测绘收费
#     BianHao                               = models.AutoField(primary_key=True)    #编号
#     BaDiDingZhuang         = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩收费标准
#     BaDiDingZhuangShuliang = models.FloatField()    #建筑用地拔地定桩数量
#     BaDiDingZhuangShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩费
#     YanXian                = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费标准
#     YanXianShuliang        = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费数量
#     YanXianShouFei         = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费
#     JunGongCeLiang         = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费标准
#     JunGongCeLiangShuliang = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费数量
#     JunGongCeLiangShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费
#     ZhuanJiaZiXun          = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费标准
#     ZhuanJiaZiXunShuliang  = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费数量
#     ZhuanJiaZiXunShouFei   = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费
#     DiTuCeHui              = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费收费标准
#     DiTuCeHuiShuliang      = models.FloatField()    #地形图测绘费收费数量
#     DiTuCeHuiShouFei       = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费
#     JiaoFeiDanWei          = models.CharField(max_length=50) #缴费单位名称
#     ShouFei                = models.DecimalField(max_digits=10,decimal_places=2)    #测绘服务费合计
#     RiQi                   = models.DateField()    #测绘服务费通知日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name


# class JiChuSheShiFei(models.Model):           #基础设施配套费
#     BianHao               = models.AutoField(primary_key=True)    #编号
#     ZhuZe                 = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅收费标准
#     ZhuZeShuliang         = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅数量
#     ZhuZeShouFei          = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅
#     FeiZhuZe              = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅收费标准
#     FeiZhuZeShuliang      = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅数量
#     FeiZhuZeShouFei       = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅
#     LinShiXiangMu         = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目收费标准
#     LinShiXiangMuShuliang = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目数量
#     LinShiXiangMuShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目
#     ShouFei               = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费合计
#     RiQi                  = models.DateField()    #基础设施配套费通知日期
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name



# class XiangMu(models.Model):            #项目情况
    # xmID = models.AutoField(primary_key=True)
    # xmBianHao                            = models.CharField(max_length=30)    #AutoField(primary_key=True, atomic = False)    #编号
    # xmMinCheng                           = models.CharField(max_length=128)         #项目名称
    # xmJianShedidian                      = models.CharField(max_length=128)    #建设地点
    # xmcreation                           = models.DateTimeField(default=timezone.now)   #创建时间
    # xmJianSheDanWei                      = models.ForeignKey(JianSheDanWei, on_delete=models.CASCADE)    #多对一 建设单位
    # xmFaGaiPiWen                 = models.ManyToManyField(FaGaiPiWen)    #多对一 发改批文
    # xmXuanZhiYiJianShu           = models.ForeignKey(XuanZhiYiJianShu, on_delete=models.CASCADE)    #多对一 选址意见书
    # xmGuoTuZhengJian             = models.ManyToManyField(GuoTuZhengJian)    #多对一 土地使用证
    # # xmGuiHuaTiaoJian       = models.ForeignKey(GuiHuaTiaoJian, on_delete=models.CASCADE)    #多对一 规划条件
    # # xmGuiHuaFangAn               = models.ForeignKey(GuiHuaFangAn, on_delete=models.CASCADE)    #多对一 规划方案
    # xmYongDiGuiHuaXuKe           = models.ForeignKey(YongDiGuiHuaXuKe, on_delete=models.CASCADE)    #多对一 用地规划许可证
    # xmShiGongTu                  = models.ForeignKey(ShiGongTu, on_delete=models.CASCADE)    #多对一 施工图
    # xmLuHuaJingGuanFangAn        = models.ForeignKey(LuHuaJingGuanFangAn, on_delete=models.CASCADE)    #多对一 绿化景观
    # xmKaiGongTongJiDengJiBiao    = models.ForeignKey(KaiGongTongJiDengJiBiao, on_delete=models.CASCADE)    #多对一 新开工统计登记表
    # # xmBaoJianBiao                = models.ForeignKey(BaoJianBiao, on_delete=models.CASCADE)    #多对一 报建表
    # xmQiangGai                   = models.ForeignKey(QiangGai, on_delete=models.CASCADE)    #多对一 墙改
    # xmRenFang                    = models.ForeignKey(RenFang, on_delete=models.CASCADE)    #多对一 人民防空
    # # xmHuanJingYingXiang          = models.ForeignKey(HuanJingYingXiang, on_delete=models.CASCADE)    #多对一 环境影响
    # xmKangZheng                  = models.ForeignKey(KangZheng, on_delete=models.CASCADE)    #多对一 抗震设防
    # # xmHuanWei                    = models.ForeignKey(HuanWei, on_delete=models.CASCADE)    #多对一 环卫审核备案登记
    # # xmDangAn                     = models.ForeignKey(DangAn, on_delete=models.CASCADE)    #多对一 报送建设工程档案责任书
    # xmJianSheGongChengGuiHuaXuKe = models.ForeignKey(JianSheGongChengGuiHuaXuKe, on_delete=models.CASCADE)    #多对一 建设工程规划许可证
    # xmJunGongCeLiang             = models.ForeignKey(JunGongCeLiang, on_delete=models.CASCADE)    #多对一 竣工测量成果
    # # xmFangChanCeHui              = models.ForeignKey(FangChanCeHui, on_delete=models.CASCADE)    #多对一  房产
    # # xmGuiHuaYanShou       = models.ForeignKey(GuiHuaYanShou, on_delete=models.CASCADE)    #多对一  规划核实
    # # xmCeHuiShouFei               = models.ForeignKey(CeHuiShouFei, on_delete=models.CASCADE)    #多对一  测绘收费
    # # xmJiChuSheShiFei             = models.ForeignKey(JiChuSheShiFei, on_delete=models.CASCADE)    #多对一 基础设施费
    # def __str__(self):              # __unicode__ on Python 2
    #     return self.name        
