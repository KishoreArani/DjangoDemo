from django.shortcuts import render,HttpResponse
from .models import Distribution_centre,product,Distribution_centre_Address,Distribution_centre_Location,Dealer,Dealer_Address,Ship

# Create your views here.

def home(request):
	return render(request,'tables/login.html')


def Distribution_centres(request):
	query_result = Distribution_centre.objects.all()
	return render(request,'tables/DC.html',{'query_result':query_result})

def products(request):
	query_result = product.objects.all()
	return render(request,'tables/product.html',{'query_result':query_result})

def DC_Address(request):
	query_result = Distribution_centre_Address.objects.all()
	return render(request,'tables/DC_Address.html',{'query_result':query_result})

def DC_Location(request):
	query_result = Distribution_centre_Location.objects.all()
	return render(request,'tables/DC_location.html',{'query_result':query_result})

def Dealers(request):
	query_result = Dealer.objects.all()
	return render(request,'tables/Dealers.html',{'query_result':query_result})

def Dealer_address(request):
	query_result = Dealer_Address.objects.all()
	return render(request,'tables/Dealer_address.html',{'query_result':query_result})

def Shipment(request):
	query_result = Ship.objects.all()
	return render(request,'tables/ships.html',{'query_result':query_result})