from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
    
class JianSheDanWei(models.Model):            #建设单位
	jianshedanwei_name                    = models.CharField(max_length=128, default='abc')    #建设单位
	jianshedanwei_dizhi                   = models.CharField(max_length=128)    #建设单位住址
	jianshedanwei_fadingdaibiaoren        = models.CharField(max_length=8)    #法定代表人
	jianshedanwei_fadingdaibiaorendianhua = models.CharField(max_length=11)   #法定代表人联系电话
	jianshedanwei_lianxiren               = models.CharField(max_length=8)  #联系人
	jianshedanwei_lianxirendianhua        = models.CharField(max_length=11)  #联系人电话
	jianshedanwei_dianhua                 = models.CharField(max_length=15)  #建设单位电话
	# def __str__(self):              # __unicode__ on Python 2
    #     return self.name

class XiangMu(models.Model):            #项目情况
    bianhao                            = models.AutoField(primary_key=True)    #编号
    mincheng                           = models.CharField(max_length=128)         #项目名称
    jianshedidian                      = models.CharField(max_length=128)    #建设地点
    jianshedanwei                      = models.ForeignKey("JianSheDanWei", on_delete=models.CASCADE,)    #多对一建设单位models
    # FaGaiPiWen_BianHao                 = models.ForeignKey(FaGaiPiWen)    #多对一发改批文models
    # XuanZhiYiJianShu_BianHao           = models.ForeignKey(XuanZhiYiJianShu)    #多对一选址意见书models
    # GuoTuZhengJian_BianHao             = models.ForeignKey(GuoTuZhengJian)    #多对一发改批文models
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
    # def __str__(self):              # __unicode__ on Python 2
    #     return self.name

