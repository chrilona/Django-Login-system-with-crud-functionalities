# from xml.etree.ElementInclude import include
from django.contrib import admin
# from django.urls import path
from django.urls import path,include
from.import views

urlpatterns = [
   path("",views.home,name="home"),
   path("",views.signup,name="signup"),
   path("",views.signin,name="signin"),
   path("",views.signout,name="signout"),
]