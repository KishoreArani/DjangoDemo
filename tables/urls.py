from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.home,name = "home"),
    path('Distribution_centres/',views.Distribution_centres,name = "Distribution_centres"),
    path('Distribution_centre_Address/',views.DC_Address,name = "Distribution_centre_Address"),
    path('products/',views.products,name = "products"),
    path('DC_Location/',views.DC_Location,name = "DC_Location"),
    path('Dealers/',views.Dealers,name = "Dealers"),
    path('Dealers_Address/',views.Dealer_address,name = "Dealer_address"),
    path('shipment/',views.Shipment,name = "shipment"),

]