from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.

def ListView(request):
	context={'items': Item.objects.all()}
	return render(request,"ItemsList.html",context)

def CreateView(request):
	form = ItemForm()
	if request.method=="POST":
		form =ItemForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect("items-list")
	context = {'form':form}
	return render (request,"ItemCreate.html",context)