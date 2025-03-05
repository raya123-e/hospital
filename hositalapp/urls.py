
from django.contrib import admin
from django.urls import path
from hositalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index,name='index'),
    path('starter/',views.starter,name='starter' ),
    path('about/',views.about,name='about' ),
    path('service/',views.service,name='service'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('appointment/',views.appointment,name='appointment'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit ,name='edit'),
    path('',views.register,name='register'),
    path('login/',views.login_view,name='login       '),
]
