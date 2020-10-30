from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',views.loginViews(),name="login_url"), 
    path('register/',views.registerview,name="register_url"),
    path('logout/',views.logoutViews,name="logout"),
]
