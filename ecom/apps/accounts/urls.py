from django.urls import path
#from .views import login_page
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('activate/<email_token>', views.activate_email, name='activate_email'),
    path('logout/', views.user_logout, name='logout'),
]
