from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views
from .views import handle_contact_crud
router = routers.DefaultRouter()
router.register( "get/" , handle_contact_crud)




urlpatterns = [
    path("",views.home),
    path("/handle/" , include(router.urls)),
    path("Accounts/get/", views.get_Accounts),
    path("Accounts/create/" ,views.create_Account),
    
]
