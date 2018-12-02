from django.forms import ModelForm
from . models import mt

class SbForm(ModelForm):
	class Meta:
		model = mt
		fields = '__all__'
		exclude = ['ljxh', 'syqsrq', 'syzzrq', 'gcnr','gcmc', 'dong','nan','xi','bei','isPrint']


class BzForm(ModelForm):
	class Meta:
		model = mt
		fields = '__all__'
		# exclude = ['ljxh', 'syqsrq', 'syzzrq', 'gcnr','gcmc', 'dong','nan','xi','bei','isPrint']