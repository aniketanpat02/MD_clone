"""
URL configuration for AniketFirst project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.core.serializers import serialize
from rest_framework.routers import DefaultRouter



from django.contrib import admin
from django.urls import path, include

from firstapp.views import (gett, get_center, create_center, update_center, delete_center, single_update, get_user,
                            get_collections, get_collection1, viaserialize)
from firstapp.views import(get_customer,get_customer1)
from firstapp.views import CenterView, CollectionView,CustomerAPIView
from firstapp.views import  CenterViewSet, CustomerViewSet , CollectionViewSet ,CenterViewSet1,Relation1ViewSet


admin.site.site_header = "Dairy Admin"
admin.site.site_title = "Dairy Admin Portal"
admin.site.index_title = "Welcome to Dairy Portal"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("firstapp.urls")),
    #path("Aniket/",include("firstapp.urls")),
    #path('about/',include("firstapp.urls")),
    #path('services/',include("firstapp.urls")),
    #path('feature',include('firstapp.urls')),
    #path('Center/',include('firstapp.urls')),
    path('center/' , get_center),
    path('center/create/' , create_center),
    path('center/viaserailize', viaserialize),
    path('center/update/<int:id>', update_center),
    path('center/delete/<int:id>', delete_center),
    path('center/updatefield/<int:id>', single_update),
    path('center/user',get_user),
    path('customer/',get_customer),
    path('customer/create',get_customer),
    path('customer/update/<int:id>/',get_customer1),
    path('collection/',get_collections),
    path('collection/update/<int:id>', get_collection1),
    path('center/list',CenterView.as_view()),
    path('collection/list',CollectionView.as_view()),
    path('customer/list',CustomerAPIView.as_view()),
    path('center/list1',CenterViewSet.as_view({'get': 'list', 'post':'create','put':'update','delete':'destroy'})),
    path('center/list2',CenterViewSet1.as_view({'get': 'list', 'post':'create','put':'update','delete':'destroy'})),
    path('customer/list1',CustomerViewSet.as_view({'get': 'list', 'post':'create','put':'update','delete':'destroy'})),
    path('collection/list1',CollectionViewSet.as_view({'get': 'list','post':'create','put':'update','delete':'destroy'})),
    path('relation/list1',Relation1ViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""
# urls.py
from django.urls import path
from .views import CenterView

urlpatterns = [
    path('centers/', CenterView.as_view(), name='center-list-create'),
]

"""