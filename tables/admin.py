from django.contrib import admin
from tables.models import Distribution_centre,product,Distribution_centre_Address,Distribution_centre_Location,Dealer,Dealer_Address,Ship
# Register your models here.
admin.site.register(Distribution_centre)
admin.site.register(product)
admin.site.register(Distribution_centre_Address)
admin.site.register(Distribution_centre_Location)
admin.site.register(Dealer)
admin.site.register(Dealer_Address)
admin.site.register(Ship)