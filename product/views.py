from django.shortcuts import render
from user.models import *
from product.models import *
from user.views import *
from order.models import *
# Create your views here.

def showProduct_detail(request,userid,cardid,variationid):
    user = User.objects.get(pk=userid)
    cart = Cart.objects.get(pk=cardid)

    listCartItem = cart.cartitem_set.all()
    listCartItem_unorder = []
    totalprice = 0
    for item in listCartItem:
        if item.isorder == False:
            listCartItem_unorder.append(item)
            totalprice += item.quantity * item.variation.sale_price
    totalprice_formatted = formatMoney(totalprice)
    variation = Variation.objects.get(pk = variationid)
    listImage = variation.product.image_set.all()
    context = {
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "variation":variation,
        "total_price": totalprice_formatted,
        "listImage":listImage,
    }
    return render(request, "homepage_cus/product-details.html", context)

def showallProduct(request,userid):
    user = User.objects.get(pk= userid)
    listVar = Variation.objects.all()
    listVar_Show = []
    for item in listVar:
        if item.active == True:
            listVar_Show.append(item)
    cart = Cart.objects.filter(user=user)
    cartt = Cart()
    listCartItem = []
    if cart.count() == 0:
        cartOb = Cart(user=user)
        cartt = cartOb
        cartOb.save()
        listCartItem = cartOb.cartitem_set.all()
    else:
        listCartItem = cart[0].cartitem_set.all()
        cartt = cart[0]
    listCartItem_unorder = []
    totalprice = 0
    for item in listCartItem:
        if item.isorder == False:
            listCartItem_unorder.append(item)
            totalprice += item.quantity * item.variation.sale_price
    totalprice_formatted = formatMoney(totalprice)
    count = listVar.count()//9

    context = {
        "range":range(count),
        "listVar": listVar,
        "cart": cartt,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted}
    return render(request,"homepage_cus/shop.html",context)