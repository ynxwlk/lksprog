from django.shortcuts import render
from . models import MengTouBiaoShi

def mt_sqdw(request):
    sqdws = MengTouBiaoShi.objects.all()
    return render(request, "mt/sqdws.html", {"sqdws":sqdws})

# Create your views here.
