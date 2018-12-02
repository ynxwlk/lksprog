from django.shortcuts import render

# Create your views here.
from .models import mt

def mt_shengbao(request):
	mts = mt.objects.all()
	return render(request, "mt/shengbao.html", {"mts":mts})