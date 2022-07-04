from django.urls import URLPattern, path
#from apps.accounts.views import login_page
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
]
