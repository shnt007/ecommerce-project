from django.urls import URLPattern, path
from .views import login_page, register, activate_email
#from . import views

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('activate/<email_token>', activate_email, name='activate_email'),
]
