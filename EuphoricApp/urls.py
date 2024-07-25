from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('products/', views.productPage, name='productPage'),
    path('contact/', views.contactPage, name='contactPage'),
    path('register/', views.register, name='registerPage'),
    path('login/', views.login, name='loginPage'),
    path('logout/', views.logout, name='logout'),
    path('accessLogin/', views.accessLogin, name='accessLoginPage'),
]
