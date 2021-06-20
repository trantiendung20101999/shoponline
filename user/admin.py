from django.contrib import admin
from user.models import *
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content","comment_date","product_name")
    def product_name(self,obj):
        return obj.variation.title
@admin.register(Love)
class LoveAdmin(admin.ModelAdmin):
    list_display = ("numberLove","product_name","trungbinh")

    def product_name(self,obj):
        return obj.variation.title

    def trungbinh(self,obj):
        variation = obj.variation
        listLove = variation.love_set.all()
        summ=0
        for love in listLove:
            summ+=love.numberLove
        return summ/len(listLove)
admin.site.register(Address)
admin.site.register(Fullname)
admin.site.register(Account)
admin.site.register(User)