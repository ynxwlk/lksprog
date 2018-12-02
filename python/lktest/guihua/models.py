from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    

class JianSheDanWei(models.Model):            #建设单位
    Name                    = models.CharField(max_length=128)    #建设单位
    DiZhi                   = models.CharField(max_length=128)    #建设单位住址
    FaDingDaiBiaoRen        = models.CharField(max_length=8)    #法定代表人
    FaDingDaiBiaoRenDianHua = models.CharField(max_length=11)   #法定代表人联系电话
    LianXiRen               = models.CharField(max_length=8)  #联系人
    LianXiRenDianHua        = models.CharField(max_length=11)  #联系人电话
    DianHua                 = models.CharField(max_length=15)  #建设单位电话
    def __str__(self):              # __unicode__ on Python 2
        return self.name
        
        
class FaGaiPiWen(models.Model):            #发改批文
    PiWen         = models.CharField(max_length=50)    #发改部门文件
    FaWenRiQi     = models.DateField()    #发改部门发文日期
    YongDiMianJi  = models.FloatField()    #发改部门文件用地面积
    JianSheGuiMo  = models.CharField(max_length=50)    #发改部门文件建筑规模
    JianZhuMianJi = models.FloatField()    #发改批文 建筑面积
    TouZi         = models.FloatField()#发改部门文件投资
    def __str__(self):              # __unicode__ on Python 2
        return self.name



class XuanZhiYiJianShu(models.Model):
    BianHao      = models.CharField(max_length=50)    #选址意见书编号
    BanZhengRiQi = models.DateField()     #选址意见书发证日期
    def __str__(self):              # __unicode__ on Python 2
       return self.name

class GuoTuZhengJian(models.Model):
    WenJian         = models.CharField(max_length=50)    #土地部门文件
    FaWengRiQi      = models.DateField()    #土地部门文件批准日期
    BianHao         = models.CharField(max_length=50)    #土地使用证号
    TuDiBanZhengRiQi    = models.DateField()    #土地部门发证日期
    YongDiMianJi    = models.FloatField()    #土地证用地面积
    YongDixinzhi    = models.CharField(max_length=50)    #土地证用地性质
    ZongDiTuBianHao = models.CharField(max_length=50)    #宗地图编号
    HeTong          = models.CharField(max_length=50)    #土地出让合同
    BeiZhu          = models.TextField()    #土地证备注
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class YongDiGuiHuaTiaoJian(models.Model):
    BianHao      = models.CharField(max_length=50)    #规划设计条件编号
    PiZhunRiQi   = models.DateField()    #规划设计条件批准日期
    WeiZhi       = models.CharField(max_length=50)    #规划设计条件地块位置
    YongDiMianJi = models.FloatField()    #规划设计条件用地面积
    YongDixinzhi = models.CharField(max_length=50)    #规划设计条件用地性质
    RongJiLu     = models.FloatField()    #规划设计条件容积率
    JianZhuMiDu  = models.FloatField()    #规划设计条件建筑密度
    LuDiLu       = models.FloatField()    #规划设计条件绿地率
    BeiZhu       = models.TextField()    #规划设计条件备注
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class GuiHuaFangAn(models.Model):
    BianHao          = models.CharField(max_length=50)    #批准的平面规划图编号
    PiZhunRiQi       = models.DateField()    #规划方案批准日期
    YongDiMianJi     = models.FloatField()    #规划方案用地面积
    JianZhuMianJi    = models.FloatField()    #规划方案建筑面积
    JiRongMianJi     = models.FloatField()    #规划方案计容面积
    ZhuZeMianJi      = models.FloatField()    #规划方案住宅面积
    GongJianMianJi   = models.FloatField()    #规划方案公建面积
    ShangYeMianJi    = models.FloatField()    #规划方案商用面积
    FeiJiRongMianJi  = models.FloatField()    #规划方案不计容面积
    DiXiaMianJi      = models.FloatField()    #规划方案地下层面积
    JiaKongCenMianJi = models.FloatField()    #规划方案架空层面积
    RongJiLu         = models.FloatField()    #规划方案容积率
    ZhanDiMianJi     = models.FloatField()    #规划方案建筑基底面积
    JianZhuMiDu      = models.FloatField()    #规划方案建筑密度
    LuDiMianJi       = models.FloatField()    #规划方案绿地面积
    LuDiLu           = models.FloatField()    #规划方案绿地率
    TingCheWei       = models.FloatField()    #规划方案停车位
    BeiZhu           = models.TextField()    #规划方案备注
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class YongDiGuiHuaXuKe(models.Model):
    ZiBianHao      = models.CharField(max_length=50)    #用地规划许分局自编号
    BaoJianRiQi    = models.DateField()    #用地规划许可报件日期
    ShangBaoRiQi   = models.DateField()    #用地规划许可报件送市局日期
    BeiZhu         = models.TextField()    #办理用地规划许可证备注
    ShengChaYiJian = models.TextField()    #办理用地规划许可证初审意见
    BianHao        = models.CharField(max_length=50)    #用地规划许可证编号
    BanZhengRiQi   = models.DateField()    #用地规划许可证办证日期
    YongDixinzhi   = models.CharField(max_length=50)    #用地规划许可证用地性质
    YongDiMianJi   = models.FloatField()    #用地规划许可证用地面积
    JianZhuMianJi  = models.FloatField()    #用地规划许可证建设规模
    LinZhengRiQi   = models.DateField()    #用地规划许可证领证日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class ShiGongTu(models.Model):
    BianHao       = models.CharField(max_length=50)    #经图审的施工图
    TuShengDanWei = models.CharField(max_length=50)  #设计单位
    TuShengRiQi   = models.DateField()    #图审日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class LuHuaJingGuanFangAn(models.Model):
    BianHao       = models.CharField(max_length=50)    #绿化景观方案
    ShengDingRiQi = models.DateField()    #绿化景观方案审定日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class KaiGongTongJiDengJiBiao(models.Model):
    KaiGongTongJi_BianHao = models.CharField(max_length=50)    #固定资产投资项目新开工统计登记表
    KaiGongTongJi_RiQi    = models.DateField()    #固定资产投资项目新开工统计登记表办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class BaoJianBiao(models.Model):
    BianHao = models.CharField(max_length=50)    #工程建设项目报建表
    RiQi    = models.DateField()    #工程建设项目报建表办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class QiangGai(models.Model):
    BianHao = models.CharField(max_length=50)    #墙改预缴款结算通知书
    RiQi    = models.DateField()    #墙改预缴款、结算通知书办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class RenFang(models.Model):
    BianHao = models.CharField(max_length=50)    #人民防空建设许可
    RiQi    = models.DateField()    #人民防空建设许可办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class HuanJingYingXiang(models.Model):
    BianHao = models.CharField(max_length=50)    #建设项目环境影响报告
    RiQi    = models.DateField()    #建设项目环境影响报告办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class KangZheng(models.Model):
    BianHao = models.CharField(max_length=50)    #抗震设防要求管理意见书
    RiQi    = models.DateField()    #抗震设防要求管理意见书办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class HuanWei(models.Model):
    BianHao = models.CharField(max_length=50)    #环卫审核备案登记
    RiQi    = models.DateField()    #环卫审核备案登记办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class DangAn(models.Model):
    BianHao = models.CharField(max_length=50)    #报送建设工程档案责任书
    RiQi    = models.DateField()    #报送建设工程档案责任书办理日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class JianSheGongChengGuiHuaXuKe(models.Model):
    BaoJianRiQi   = models.DateField()    #建设工程规划许可报件日期
    ZiBianHao     = models.CharField(max_length=50)    #建设工程规划许分局自编号
    ShangBaoRiQi  = models.DateField()    #建设工程规划许可报件送市局日期
    BeiZhu        = models.CharField(max_length=50)    #办理建设工程规划许可证备注
    YiJian        = models.TextField()    #办理建设工程规划许可证初审意见
    BianHao       = models.CharField(max_length=50)    #建设工程规划许编号
    JianSheGuiMo  = models.TextField()    #建设工程规划许建设规模
    JianZhuMianJi = models.FloatField()    #建设工程规划许建设面积
    BeiZhu        = models.TextField()    #建设项目审批内容明细表
    BanZhengRiQi  = models.DateField()    #建设工程规划许办证日期
    LinZhengRiQi  = models.DateField()    #建设工程规划许可证领证日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name



class JunGongCeLiang(models.Model):
    BianHao      = models.CharField(max_length=50)    #竣工测量成果资料编号
    RiQi         = models.DateField()    #竣工测量成果资料出图日期
    YongDiMianJi = models.FloatField()    #竣工用地面积
    ZhanDiMianJi = models.FloatField()    #竣测建筑占地面积
    JianZhuMiDu  = models.FloatField()    #竣工建筑密度
    LuDiMianJi   = models.FloatField()    #竣工绿地面积
    LuDiLu       = models.FloatField()    #竣工绿地率
    TingCheWei   = models.FloatField()    #竣工停车位
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class FangChanCeHui(models.Model):
    BianHao          = models.CharField(max_length=50)    #房产面积测绘报告书编号
    RiQi             = models.DateField()    #房产面积测绘报告书办理日期
    diShangmiji      = models.FloatField()    #竣工地上建筑面积
    JiRongMianJi     = models.FloatField()    #竣工计容面积
    ZhuZeMianJi      = models.FloatField()    #竣工住宅面积
    GongJianMianJi   = models.FloatField()    #竣工公建面积
    ShangYeMianJi    = models.FloatField()    #竣工商用面积
    FeiJiRongMianJi  = models.FloatField()    #竣工不计容面积
    DiXiaMianJi      = models.FloatField()    #竣工地下层面积
    JiaKongCenMianJi = models.FloatField()    #竣工架空层面积
    RongJiLu         = models.FloatField()    #竣工容积率
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class JunGongGuiHuaYanShou(models.Model):
    BaoJianRiQi     = models.DateField()    #竣工验收报件日期
    ZiBianHao       = models.CharField(max_length=50)    #竣工验收分局自编号
    ShangBaoRiQi    = models.DateField()    #竣工验收报件送市局日期 
    GenZongFuWuBiao = models.CharField(max_length=50)    #验线表或跟踪服务表
    BeiZhu          = models.TextField()    #验收备注
    YiJian          = models.TextField()    #竣工验收合格证初审意见
    BianHao         = models.CharField(max_length=50)    #竣工验收合格证编号
    BanZhengRiQi    = models.DateField()    #竣工验收合格证办证日期
    LinZhengRiQi    = models.DateField()    #竣工验收合格证领证日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class ShouFeiBiaoZhun(models.Model):
    BaDiDingZhuang = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩收费标准
    YanXian        = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费标准
    JunGongCeLiang = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费标准
    ZhuanJiaZiXun  = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费标准
    DiTuCeHui      = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费收费标准
    ZhuZe          = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅收费标准
    FeiZhuZe       = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅收费标准
    LinShiXiangMu  = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目收费标准
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class CeHuiShouFei(models.Model):
    BaDiDingZhuang         = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩收费标准
    BaDiDingZhuangShuliang = models.FloatField()    #建筑用地拔地定桩数量
    BaDiDingZhuangShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩费
    YanXian                = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费标准
    YanXianShuliang        = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费数量
    YanXianShouFei         = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费
    JunGongCeLiang         = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费标准
    JunGongCeLiangShuliang = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费数量
    JunGongCeLiangShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费
    ZhuanJiaZiXun          = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费标准
    ZhuanJiaZiXunShuliang  = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费数量
    ZhuanJiaZiXunShouFei   = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费
    DiTuCeHui              = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费收费标准
    DiTuCeHuiShuliang      = models.FloatField()    #地形图测绘费收费数量
    DiTuCeHuiShouFei       = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费
    JiaoFeiDanWei          = models.CharField(max_length=50) #缴费单位名称
    ShouFei                = models.DecimalField(max_digits=10,decimal_places=2)    #测绘服务费合计
    RiQi                   = models.DateField()    #测绘服务费通知日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class JiChuSheShiFei(models.Model):
    ZhuZe                 = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅收费标准
    ZhuZeShuliang         = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅数量
    ZhuZeShouFei          = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅
    FeiZhuZe              = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅收费标准
    FeiZhuZeShuliang      = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅数量
    FeiZhuZeShouFei       = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅
    LinShiXiangMu         = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目收费标准
    LinShiXiangMuShuliang = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目数量
    LinShiXiangMuShouFei  = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目
    ShouFei               = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费合计
    RiQi                  = models.DateField()    #基础设施配套费通知日期
    def __str__(self):              # __unicode__ on Python 2
        return self.name
 
 
class XiangMu(models.Model):            #项目情况
    BianHao                            = models.AutoField(primary_key=True)    #编号
    MinCheng                           = models.CharField(max_length=128)         #项目名称
    JianShedidian                      = models.CharField(max_length=128)    #建设地点
    JianSheDanWei                      = models.ForeignKey(JianSheDanWei)    #多对一建设单位models
    FaGaiPiWen                = models.ManyToManyField(FaGaiPiWen)    #多对一发改批文models
    XuanZhiYiJianShu            = models.ForeignKey(XuanZhiYiJianShu)    #多对一选址意见书models
    GuoTuZhengJian             = models.ManyToManyField(GuoTuZhengJian)    #多对一发改批文models
    # YongDiGuiHuaTiaoJian_BianHao       = models.ForeignKey(YongDiGuiHuaTiaoJian)    #多对一发改批文models
    # GuiHuaFangAn_BianHao               = models.ForeignKey(GuiHuaFangAn)    #多对一发改批文models
    # YongDiGuiHuaXuKe_BianHao           = models.ForeignKey(YongDiGuiHuaXuKe)    #多对一发改批文models
    # ShiGongTu_BianHao                  = models.ForeignKey(ShiGongTu)    #多对一发改批文models
    # LuHuaJingGuanFangAn_BianHao        = models.ForeignKey(LuHuaJingGuanFangAn)    #多对一发改批文models
    # KaiGongTongJiDengJiBiao_BianHao    = models.ForeignKey(KaiGongTongJiDengJiBiao)    #多对一发改批文models
    # BaoJianBiao_BianHao                = models.ForeignKey(BaoJianBiao)    #多对一发改批文models
    # QiangGai_BianHao                   = models.ForeignKey(QiangGai)    #多对一发改批文models
    # RenFang_BianHao                    = models.ForeignKey(RenFang)    #多对一发改批文models
    # HuanJingYingXiang_BianHao          = models.ForeignKey(HuanJingYingXiang)    #多对一发改批文models
    # KangZheng_BianHao                  = models.ForeignKey(KangZheng)    #多对一发改批文models
    # HuanWei_BianHao                    = models.ForeignKey(HuanWei)    #多对一发改批文models
    # DangAn_BianHao                     = models.ForeignKey(DangAn)    #多对一发改批文models
    # JianSheGongChengGuiHuaXuKe_BianHao = models.ForeignKey(JianSheGongChengGuiHuaXuKe)    #多对一发改批文models
    # JunGongCeLiang_BianHao             = models.ForeignKey(JunGongCeLiang)    #多对一发改批文models
    # FangChanCeHui_BianHao              = models.ForeignKey(FangChanCeHui)    #多对一发改批文models
    # JunGongGuiHuaYanShou_BianHao       = models.ForeignKey(JunGongGuiHuaYanShou)    #多对一发改批文models
    # CeHuiShouFei_BianHao               = models.ForeignKey(CeHuiShouFei)    #多对一发改批文models
    # JiChuSheShiFei_BianHao             = models.ForeignKey(JiChuSheShiFei)    #多对一发改批文models
    def __str__(self):              # __unicode__ on Python 2
        return self.name
