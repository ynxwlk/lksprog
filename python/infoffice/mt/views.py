from django.shortcuts import render
from django.http import HttpResponse
from . forms import SbForm, BzForm
from . models import mt

# Create your views here.
def shenbao(request):
    if request.method == 'POST':
        form = SbForm(request.POST)
        if form.is_valid():
            sb_info = form.save()
            sb_info.save()
            return HttpResponse('提交成功，请至窗口办业务！')
    else:
        form = SbForm()
    return render(request, 'mt/sb.html', {'form_info': form})

def banzheng(request):
    if request.method == 'POST':
        form = BzForm(request.POST)
        if form.is_valid():
            sb_info = form.save()
            sb_info.save()
            return HttpResponse('证件办理完成。')
    else:
        form = BzForm()
    return render(request, 'mt/bz.html', {'form_info': form})

def dbdw(request):
    dws = mt.objects.all()
    return render(request, "mt/dbdw.html", {"dws":dws})