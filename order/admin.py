from django.contrib import admin
from order.models import *
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_date","total_price","type_pay","address_ship","ischeck")

    def total_price(self,obj):
        return obj.payment.total_price
    def type_pay(self,obj):
        return obj.payment.type
    def address_ship(self,obj):
        return obj.shipment.address

admin.site.register(Shipment)
admin.site.register(Payment)