from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns = [
    path("",views.Centerdata, name="Home page"),
    path('buffelo', views.buffelo, name="buffelo page"),
    path('cow/', views.cow ,name= "cow page"),
    path("contact/",views.contact , name="contact page"),
    path('about/',views.about , name="about page"),
    path('services/',views.services ,name="service page"),
    path('list',views.list1 , name="list page"),
    path('Center',views.centerr, name="center"),
    #path('/<int:code>/' ,views.get_user, name="by id"),
   # path('/<int:code>/<str:name>',views.get_user, name= "bynameid"),
    path('/<str:name>',views.get_user,name="by name")

]
