from django.shortcuts import render
from user.models import *
from product.models import *
from order.models import *
from user.views import *
# Create your views here.

def addToCart(request,userid,variationid,cartid,quantity):
    user = User.objects.get(pk = userid)
    variation = Variation.objects.get(pk = variationid)
    cart = Cart.objects.get(pk=cartid)

    listItem = cart.cartitem_set.all()
    check = True
    for item in listItem:
        if item.variation.id is variation.id and item.isorder == False:
            CartItem.objects.filter(pk=item.id).update(quantity=item.quantity + 1)
            check = False

    if check is True:
        cartitem = CartItem(quantity = quantity,variation = variation,cart = cart)
        cartitem.save()

    listVar = Variation.objects.all()
    listVar_Show =[]
    for item in listVar:
        if item.active == True:
            listVar_Show.append(item)
    listCartItem = cart.cartitem_set.all()
    listCartItem_unorder=[]
    totalprice=0
    for item in listCartItem:
        if item.isorder == False:
            listCartItem_unorder.append(item)
            totalprice += item.quantity * item.variation.sale_price
    totalprice_formatted = formatMoney(totalprice)
    context = {
        "listVar": listVar_Show,
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price":totalprice_formatted
        }
    return render(request, "homepage_cus/index.html", context)
def checkout(request,userid,cardid):
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
    context = {
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted
    }
    return render(request, "homepage_cus/checkout.html", context)
def removeItem(request,userid,cardid,itemid):
    user = User.objects.get(pk=userid)
    cart = Cart.objects.get(pk=cardid)
    cartItem = CartItem.objects.get(pk=itemid)
    cartItem.delete()
    listCartItem = cart.cartitem_set.all()
    listCartItem_unorder = []
    totalprice = 0
    for item in listCartItem:
        if item.isorder == False:
            listCartItem_unorder.append(item)
            totalprice += item.quantity * item.variation.sale_price
    totalprice_formatted = formatMoney(totalprice)
    context = {
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted,
    }
    return render(request, "homepage_cus/cart.html", context)

def showCart(request,userid,cardid):
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
    context = {
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted,
    }
    return render(request ,"homepage_cus/cart.html",context)

def completeCheckout(request,userid,cardid):

    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    number = request.POST.get("number")
    lane = request.POST.get("lane")
    street = request.POST.get("street")
    district = request.POST.get("district")
    city = request.POST.get("city")
    phonenumber = request.POST.get("phonenumber")
    type = request.POST.get("type_checkout")

    fullname = Fullname(firstname=firstname,lastname=lastname,midname="")
    fullname.save()
    address = Address(number=number,lane=lane,street=street,district=district,city=city)
    address.save()
    str_address = "".join((number,lane,street,district,city))
    shipment = Shipment(address =str_address,price = 100000)
    shipment.save()

    User.objects.filter(pk=userid).update(fullname=fullname,address=address,phonenumber=phonenumber)
    cart = Cart.objects.get(pk=cardid)
    listCartItem = cart.cartitem_set.all()
    listCartItem_unorder = []
    totalprice = 0
    for item in listCartItem:
        CartItem.objects.filter(pk=item.id).update(isorder=True)
        if item.isorder == False:
            listCartItem_unorder.append(item)
            totalprice += item.quantity * item.variation.sale_price
    totalprice_formatted = formatMoney(totalprice)
    payment = Payment(type=type,total_price=totalprice,shipment=shipment,cart=cart)
    payment.save()
    user = User.objects.get(pk=userid)
    order = Order(order_description="",cart=cart,payment=payment,shipment=shipment)
    order.save()
    context = {
        "cart": cart,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted,
    }
    return render(request, "homepage_cus/cart.html", context)