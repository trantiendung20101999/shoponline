from django.shortcuts import render
from django.views import View
from product.models import *
from user.models import *
from user.views import *
# Create your views here.
class HomeView(View):
    def get(self , request):
        listVar = Variation.objects.all()
        listVar_Show = []
        for item in listVar:
            if item.active == True:
                listVar_Show.append(item)

        return render(request,'homepage_cus/index.html',{"listVar":listVar_Show})

def showlogin(request):
    return render(request,'homepage_cus/login.html')

def showregister(request):
    return render(request,'homepage_cus/register.html')

def backtoadmin(request):

        date_now = datetime.datetime.now().date()
        day = datetime.datetime.now().date().day
        day = day - 1
        date_last = date_now.replace(day=day)
        listOrder = Order.objects.all()
        list_onday = []
        list_order_lastday = []
        money_onday = 0
        money_lastday = 0
        cloth_order_cost = 0
        book_order_cost = 0
        elec_order_cost = 0
        order_jan = 0
        order_feb = 0
        order_mar = 0
        order_apr = 0
        order_may = 0
        order_jun = 0
        order_jul = 0
        order_aug = 0
        order_sep = 0
        order_oct = 0
        order_nov = 0
        order_dec = 0
        list_order_bymonth = []
        for order in listOrder:
            if (order.order_date.month == 1):
                order_jan += order.payment.total_price
            if (order.order_date.month == 2):
                order_feb += order.payment.total_price
            if (order.order_date.month == 3):
                order_mar += order.payment.total_price
            if (order.order_date.month == 4):
                order_apr += order.payment.total_price
            if (order.order_date.month == 5):
                order_may += order.payment.total_price
            if (order.order_date.month == 6):
                order_jun += order.payment.total_price
            if (order.order_date.month == 7):
                order_jul += order.payment.total_price
            if (order.order_date.month == 8):
                order_aug += order.payment.total_price
            if (order.order_date.month == 9):
                order_sep += order.payment.total_price
            if (order.order_date.month == 10):
                order_oct += order.payment.total_price
            if (order.order_date.month == 11):
                order_nov += order.payment.total_price
            if (order.order_date.month == 12):
                order_dec += order.payment.total_price
            listCartItem = order.cart.cartitem_set.all()
            for item in listCartItem:
                if item.variation.product.discriminator == "quanao":
                    cloth_order_cost += item.variation.sale_price
                elif item.variation.product.discriminator == "dientu":
                    elec_order_cost += item.variation.sale_price
                else:
                    book_order_cost += item.variation.sale_price
            if order.order_date.date() == date_now:
                list_onday.append(order)
                money_onday += order.payment.total_price
            if order.order_date.date() == date_last:
                list_order_lastday.append(order)
                money_lastday += order.payment.total_price
        order_change = len(list_onday) - len(list_order_lastday)
        list_order_bymonth.append(order_jan)
        list_order_bymonth.append(order_feb)
        list_order_bymonth.append(order_mar)
        list_order_bymonth.append(order_apr)
        list_order_bymonth.append(order_may)
        list_order_bymonth.append(order_jun)
        list_order_bymonth.append(order_jul)
        list_order_bymonth.append(order_aug)
        list_order_bymonth.append(order_sep)
        list_order_bymonth.append(order_oct)
        list_order_bymonth.append(order_nov)
        list_order_bymonth.append(order_dec)
        listComment = Comment.objects.all()
        list_comment_onday = []
        list_comment_lastday = []
        for comment in listComment:
            if comment.comment_date.date() == date_now:
                list_comment_onday.append(comment)
            if comment.comment_date.date() == date_last:
                list_comment_lastday.append(comment)
        comment_change = len(list_comment_onday) - len(list_comment_lastday)

        listLove = Love.objects.all()
        love_onday = 0
        count_onday = 0
        love_lastday = 0
        count_lastday = 0
        for love in listLove:
            if love.love_date.date() == date_now:
                love_onday += love.numberLove
                count_onday += 1
            if love.love_date.date() == date_last:
                love_lastday += love.numberLove
                count_lastday += 1
        love_onday_ave = round(love_onday / count_onday,1)
        if (count_lastday != 0):
            love_lastday_ave = love_lastday / count_lastday
        else:
            love_lastday_ave = "Không có rate "
        if (money_lastday != 0):
            money_change = round(((money_onday / money_lastday) * 100), 1)
        else:
            money_change = "Không có đơn vào ngày trước "
        listVar = Variation.objects.all()
        max = 0
        varId = 0
        for var in listVar:
            listLove = var.love_set.all()

            lovetb = 0
            for love in listLove:
                lovetb += love.numberLove
            if (len(listLove) != 0):
                lovetb = lovetb / len(listLove)
            else:
                lovetb = 0
            if max < lovetb:
                max = lovetb
                varId = var.id
        context = {"money_onday": money_onday,
                   "cloth_cost": cloth_order_cost,
                   "book_cost": book_order_cost,
                   "elec_cost": elec_order_cost,
                   "list_cost": list_order_bymonth,
                   "varid": varId,
                   "money_change": money_change, "love_onday": love_onday_ave, "love_lastday": love_lastday_ave,
                   "listOrder": list_onday, "order_change": order_change, "comment_change": comment_change,
                   "listComment": list_comment_onday}
        return render(request, "homepage/index.html", context)
def goToHome(request,userid):
    user = User.objects.get(pk=userid)
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
    context = {
        "listVar": listVar_Show,
        "cart": cartt,
        "listItem": listCartItem_unorder,
        "user": user,
        "total_price": totalprice_formatted}
    return render(request, "homepage_cus/index.html", context)

