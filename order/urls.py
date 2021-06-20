
from django.urls import path
from . import views
app_name="order"
urlpatterns = [
    path('addToCart/<int:userid>/<int:variationid>/<int:cartid>/<int:quantity>', views.addToCart , name="addtoCart"),
    path('showCart/<int:userid>/<int:cardid>', views.showCart, name="showCart"),
    path('removeItem/<int:userid>/<int:cardid>/<int:itemid>', views.removeItem, name="removeItem"),
    path('showCheckout/<int:userid>/<int:cardid>', views.checkout, name="showCheckout"),
    path('checkout/<int:userid>/<int:cardid>', views.completeCheckout, name="checkout"),
]
