
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from VegiApp.api import *

urlpatterns = [
    path('admin-site/', include('VegiApp.urls')),
    path('', views.login, name = "Login"),
    path('logout', views.logout, name = "LogOut"),
    path('deletesessions/', views.delSessions, name = "DelSessions"),

    # API Urls
    path('api/get-vegi-fruits/', VegiFruitList.as_view(), name = "VegiFruitsList"),
    path('api/get-vegifruits-by-cat/<int:catId>', AllVegiFruitsByCatList.as_view(), name = "AllVegiFruitsByCatList"),
    path('api/get-single-vegifruit/<int:vegifruitId>', GetSingleVegiFruit.as_view(), name = "GetSingleVegiFruit"),

    # API AUTHs
    path('api/login/', APILogin.as_view(), name = 'APILogin'),
    path('api/user/', APIUser.as_view(), name = 'APIUser'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)