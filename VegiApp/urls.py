from django.contrib import admin
from django.urls import path, include
from django.http import HttpRequest
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name = "Dashboard"),
    path('icons/', views.icons, name = "Icons"),
    # path('map/', views.map, name = "Map"),
    # path('notifications/', views.notifications, name = "Notifications"),
    # path('tables/', views.tables, name = "Tables"),
    # path('typography/', views.typography, name = "Typography"),
    # User's URLs

    # Users
    path('user/', views.user, name = "User"),
    # path('add-user/', views.addUser, name = "AddUser"),
    # path('set-password/<str:userToken>', views.setPassword, name = "SetPassword"),
    # path('save-password/', views.savePassword, name = "SavePassword"),
    # path('delete-user/', views.deleteUser, name = "DeleteUser"),
    # path('edit-user/', views.editUser, name = "EditUser"),
    # path('save-user/', views.saveUser, name = "SaveUser"),
    # path('checkuserexistance/', views.checkUserExists, name = "CheckUserExists"),
    # path('user-profile/', views.userProfile, name = "UserProfile"),
    # path('user-deletion-request/', views.UserDeletionRequest, name = "UserDelRequest"),

    # Categories
    path('categories/', views.categories, name = "Categories"),
    # Vegis
    path('vegis/', views.vegis, name = "Vegis"),
    path('add-vegi-fruits/', views.addVegiFruits, name = "AddVegiFruits"),
    path('delete-vegi-fruits/', views.deleteVegiFruits, name = "DeleteVegiFruits"),
    path('edit-vegi-fruits/', views.editVegiFruits, name = "EditVegiFruits"),
    path('save-vegi-fruits/', views.saveVegiFruits, name = "SaveVegiFruits"),
]