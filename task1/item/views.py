from django.shortcuts import render
from .models import Item
# Create your views here.

def ListView(request):
	context={'items': Item.objects.all()}
	return render(request,"ItemsList.html",context)