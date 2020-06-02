from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('register_user/',views.register_user,name='register_user'),
    path('logout/',views.logout,name='logout')
]