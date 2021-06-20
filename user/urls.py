
from django.urls import path
from . import views
app_name="users"
urlpatterns = [
    path('checklogin', views.checklogin , name="checklogin"),
    path('register', views.register, name="register"),
    path('addReact/<int:userid>/<int:cardid>/<int:variationid>', views.addReact, name="addReact"),

]
