
from django.urls import path
from . import views
app_name="product"
urlpatterns = [
    # path('addToCart/<int:userid>/<int:variationid>/<int:cartid>/<int:quantity>', views.addToCart , name="addtoCart"),
    path('showShop/<int:userid>', views.showallProduct, name="showShop"),
    path('showProduct/<int:userid>/<int:cardid>/<int:variationid>', views.showProduct_detail, name="showProduct"),

]
