
from django.contrib import admin
from django.urls import path
from hositalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('starter/',views.starter,name='starter' ),
]
