from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('login/',views.login),
    path('signup/',views.signup),
    path('user_home/',views.user,name='user_home'),
]