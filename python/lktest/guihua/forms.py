# from django import forms
    
# class JianSheDanWeiForm(forms.Form):            #建设单位
#     JianSheDanWei           = forms.CharField(label='',max_length=128)    #建设单位
#     DiZhi                   = forms.CharField(label='',max_length=128)    #建设单位住址
#     FaDingDaiBiaoRen        = forms.CharField(label='',max_length=8)    #法定代表人
#     FaDingDaiBiaoRenDianHua = forms.CharField(label='',max_length=11)   #法定代表人联系电话
#     LianXiRen               = forms.CharField(label='',max_length=8)  #联系人
#     LianXiRenDianHua        = forms.CharField(label='',max_length=11)  #联系人电话
#     DanWeiDianHua           = forms.CharField(label='',max_length=15)  #建设单位电话            
        
# class FaGaiPiWenForm(forms.Form):            #发改批文
#     FaGaiPiWen    = forms.CharField(label='',max_length=50)    #发改部门文件
#     FaWenRiQi     = models.DateField()    #发改部门发文日期
#     YongDiMianJi  = models.FloatField()    #发改部门文件用地面积
#     JianSheGuiMo  = forms.CharField(label='',max_length=50)    #发改部门文件建筑规模
#     JianZhuMianJi = models.FloatField()    #发改批文 建筑面积
#     TouZi         = models.FloatField()#发改部门文件投资

# class XuanZhiYiJianShuForm(forms.Form):
#     BianHao      = forms.CharField(label='',max_length=50)    #选址意见书编号
#     BanZhengRiQi = models.DateField()     #选址意见书发证日期

# class GuoTuZhengJianForm(forms.Form):
#     WenJian         = forms.CharField(label='',max_length=50)    #土地部门文件
#     FaWengRiQi      = models.DateField()    #土地部门文件批准日期
#     BianHao         = forms.CharField(label='',max_length=50)    #土地使用证号
#     BanZhengRiQi    = models.DateField()    #土地部门发证日期
#     YongDiMianJi    = models.FloatField()    #土地证用地面积
#     YongDixinzhi    = forms.CharField(label='',max_length=50)    #土地证用地性质
#     ZongDiTuBianHao = forms.CharField(label='',max_length=50)    #宗地图编号
#     HeTong          = forms.CharField(label='',max_length=50)    #土地出让合同
#     BeiZhu          = models.TextField()    #土地证备注
    
# class YongDiGuiHuaTiaoJianForm(forms.Form):
#     BianHao      = forms.CharField(label='',max_length=50)    #规划设计条件编号
#     PiZhunRiQi   = models.DateField()    #规划设计条件批准日期
#     WeiZhi       = forms.CharField(label='',max_length=50)    #规划设计条件地块位置
#     YongDiMianJi = models.FloatField()    #规划设计条件用地面积
#     YongDixinzhi = forms.CharField(label='',max_length=50)    #规划设计条件用地性质
#     RongJiLu     = models.FloatField()    #规划设计条件容积率
#     JianZhuMiDu  = models.FloatField()    #规划设计条件建筑密度
#     LuDiLu       = models.FloatField()    #规划设计条件绿地率
#     BeiZhu       = models.TextField()    #规划设计条件备注
    

# class GuiHuaFangAnForm(forms.Form):
#     BianHao          = forms.CharField(label='',max_length=50)    #批准的平面规划图编号
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
    
# class YongDiGuiHuaXuKeForm(forms.Form):
#     ZiBianHao      = forms.CharField(label='',max_length=50)    #用地规划许分局自编号
#     BaoJianRiQi    = models.DateField()    #用地规划许可报件日期
#     ShangBaoRiQi   = models.DateField()    #用地规划许可报件送市局日期
#     BeiZhu         = models.TextField()    #办理用地规划许可证备注
#     ShengChaYiJian = models.TextField()    #办理用地规划许可证初审意见
#     BianHao        = forms.CharField(label='',max_length=50)    #用地规划许可证编号
#     BanZhengRiQi   = models.DateField()    #用地规划许可证办证日期
#     YongDixinzhi   = forms.CharField(label='',max_length=50)    #用地规划许可证用地性质
#     YongDiMianJi   = models.FloatField()    #用地规划许可证用地面积
#     JianZhuMianJi  = models.FloatField()    #用地规划许可证建设规模
#     LinZhengRiQi   = models.DateField()    #用地规划许可证领证日期    

# class ShiGongTuForm(forms.Form):
#     BianHao       = forms.CharField(label='',max_length=50)    #经图审的施工图
#     TuShengDanWei = forms.CharField(label='',max_length=50)  #设计单位
#     TuShengRiQi   = models.DateField()    #图审日期
    
# class LuHuaJingGuanFangAnForm(forms.Form):
#     BianHao       = forms.CharField(label='',max_length=50)    #绿化景观方案
#     ShengDingRiQi = models.DateField()    #绿化景观方案审定日期
    
# class KaiGongTongJiDengJiBiaoForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #固定资产投资项目新开工统计登记表
#     RiQi    = models.DateField()    #固定资产投资项目新开工统计登记表办理日期
    
# class BaoJianBiaoForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #工程建设项目报建表
#     RiQi    = models.DateField()    #工程建设项目报建表办理日期
    
# class QiangGaiForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #墙改预缴款结算通知书
#     RiQi    = models.DateField()    #墙改预缴款、结算通知书办理日期
    
# class RenFangForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #人民防空建设许可
#     RiQi    = models.DateField()    #人民防空建设许可办理日期
    
# class HuanJingYingXiangForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #建设项目环境影响报告
#     RiQi = models.DateField()    #建设项目环境影响报告办理日期
    
# class KangZhengForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #抗震设防要求管理意见书
#     RiQi    = models.DateField()    #抗震设防要求管理意见书办理日期
    
# class HuanWeiForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #环卫审核备案登记
#     RiQi    = models.DateField()    #环卫审核备案登记办理日期
    
# class DangAnForm(forms.Form):
#     BianHao = forms.CharField(label='',max_length=50)    #报送建设工程档案责任书
#     RiQi    = models.DateField()    #报送建设工程档案责任书办理日期
    
# class JianSheGongChengGuiHuaXuKeForm(forms.Form):
#     BaoJianRiQi   = models.DateField()    #建设工程规划许可报件日期
#     ZiBianHao     = forms.CharField(label='',max_length=50)    #建设工程规划许分局自编号
#     ShangBaoRiQi  = models.DateField()    #建设工程规划许可报件送市局日期
#     BeiZhu        = forms.CharField(label='',max_length=50)    #办理建设工程规划许可证备注
#     YiJian        = models.TextField()    #办理建设工程规划许可证初审意见
#     BianHao       = forms.CharField(label='',max_length=50)    #建设工程规划许编号
#     JianSheGuiMo  = models.TextField()    #建设工程规划许建设规模
#     JianZhuMianJi = models.FloatField()    #建设工程规划许建设面积
#     BeiZhu        = models.TextField()    #建设项目审批内容明细表
#     BanZhengRiQi  = models.DateField()    #建设工程规划许办证日期
#     LinZhengRiQi  = models.DateField()    #建设工程规划许可证领证日期

# class JunGongCeLiangForm(forms.Form):
#     BianHao      = forms.CharField(label='',max_length=50)    #竣工测量成果资料编号
#     RiQi         = models.DateField()    #竣工测量成果资料出图日期
#     YongDiMianJi = models.FloatField()    #竣工用地面积
#     ZhanDiMianJi = models.FloatField()    #竣测建筑占地面积
#     JianZhuMiDu  = models.FloatField()    #竣工建筑密度
#     LuDiMianJi   = models.FloatField()    #竣工绿地面积
#     LuDiLu       = models.FloatField()    #竣工绿地率
#     TingCheWei   = models.FloatField()    #竣工停车位
    
# class FangChanCeHuiForm(forms.Form):
#     BianHao          = forms.CharField(label='',max_length=50)    #房产面积测绘报告书编号
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

# class JunGongGuiHuaYanShouForm(forms.Form):
#     BaoJianRiQi     = models.DateField()    #竣工验收报件日期
#     ZiBianHao       = forms.CharField(label='',max_length=50)    #竣工验收分局自编号
#     ShangBaoRiQi    = models.DateField()    #竣工验收报件送市局日期 
#     GenZongFuWuBiao = forms.CharField(label='',max_length=50)    #验线表或跟踪服务表
#     BeiZhu          = models.TextField()    #验收备注
#     YiJian          = models.TextField()    #竣工验收合格证初审意见
#     BianHao         = forms.CharField(label='',max_length=50)    #竣工验收合格证编号
#     BanZhengRiQi    = models.DateField()    #竣工验收合格证办证日期
#     LinZhengRiQi    = models.DateField()    #竣工验收合格证领证日期
    
# class ShouFeiBiaoZhunForm(forms.Form):
#     BaDiDingZhuang = models.DecimalField(max_digits=10,decimal_places=2)    #建筑用地拔地定桩收费标准
#     YanXian        = models.DecimalField(max_digits=10,decimal_places=2)    #建筑物验线费收费标准
#     JunGongCeLiang = models.DecimalField(max_digits=10,decimal_places=2)    #竣工图测量费收费标准
#     ZhuanJiaZiXun  = models.DecimalField(max_digits=10,decimal_places=2)    #专家咨询费收费标准
#     DiTuCeHui      = models.DecimalField(max_digits=10,decimal_places=2)    #地形图测绘费收费标准
#     ZhuZe          = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费住宅收费标准
#     FeiZhuZe       = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费非住宅收费标准
#     LinShiXiangMu  = models.DecimalField(max_digits=10,decimal_places=2)    #基础设施配套费临时项目收费标准
    

# class CeHuiShouFeiForm(forms.Form):
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
#     JiaoFeiDanWei          = forms.CharField(label='',max_length=50) #缴费单位名称
#     ShouFei                = models.DecimalField(max_digits=10,decimal_places=2)    #测绘服务费合计
#     RiQi                   = models.DateField()    #测绘服务费通知日期
    

# class JiChuSheShiFeiForm(forms.Form):
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
     
 
# class XiangMuForm(forms.Form):            #项目情况
#     BianHao                    = models.AutoField(primary_key=True)    #编号
#     MinCheng                   = forms.CharField(label='',max_length=128)         #项目名称
#     JianShedidian              = forms.CharField(label='',max_length=128)    #建设地点
#     JianSheDanWei              = models.ForeignKey(JianSheDanWei)    #多对一建设单位models
#     FaGaiPiWen                 = models.ForeignKey(FaGaiPiWen)    #多对一发改批文models
#     XuanZhiYiJianShu           = models.ForeignKey(XuanZhiYiJianShu.BianHao)    #多对一选址意见书models
#     GuoTuZhengJian             = models.ForeignKey(GuoTuZhengJian.BianHao)    #多对一发改批文models
#     YongDiGuiHuaTiaoJian       = models.ForeignKey(YongDiGuiHuaTiaoJian.BianHao)    #多对一发改批文models
#     GuiHuaFangAn               = models.ForeignKey(GuiHuaFangAn.BianHao)    #多对一发改批文models
#     YongDiGuiHuaXuKe           = models.ForeignKey(YongDiGuiHuaXuKe.BianHao)    #多对一发改批文models
#     ShiGongTu                  = models.ForeignKey(ShiGongTu.BianHao)    #多对一发改批文models
#     LuHuaJingGuanFangAn        = models.ForeignKey(LuHuaJingGuanFangAn.BianHao)    #多对一发改批文models
#     KaiGongTongJiDengJiBiao    = models.ForeignKey(KaiGongTongJiDengJiBiao.BianHao)    #多对一发改批文models
#     BaoJianBiao                = models.ForeignKey(BaoJianBiao.BianHao)    #多对一发改批文models
#     QiangGai                   = models.ForeignKey(QiangGai.BianHao)    #多对一发改批文models
#     RenFang                    = models.ForeignKey(RenFang.BianHao)    #多对一发改批文models
#     HuanJingYingXiang          = models.ForeignKey(HuanJingYingXiang.BianHao)    #多对一发改批文models
#     KangZheng                  = models.ForeignKey(KangZheng.BianHao)    #多对一发改批文models
#     HuanWei                    = models.ForeignKey(HuanWei.BianHao)    #多对一发改批文models
#     DangAn                     = models.ForeignKey(DangAn.BianHao)    #多对一发改批文models
#     JianSheGongChengGuiHuaXuKe = models.ForeignKey(JianSheGongChengGuiHuaXuKe.BianHao)    #多对一发改批文models
#     JunGongCeLiang             = models.ForeignKey(JunGongCeLiang.BianHao)    #多对一发改批文models
#     FangChanCeHui              = models.ForeignKey(FangChanCeHui.BianHao)    #多对一发改批文models
#     JunGongGuiHuaYanShou       = models.ForeignKey(JunGongGuiHuaYanShou.BianHao)    #多对一发改批文models
#     CeHuiShouFei               = models.ForeignKey(CeHuiShouFei.BianHao)    #多对一发改批文models
#     JiChuSheShiFei             = models.ForeignKey(JiChuSheShiFei.BianHao)    #多对一发改批文models
#     