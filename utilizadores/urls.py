from django.urls import path, include
from .views import login_action
from .views import logout_action

from . import views

app_name = 'utilizadores'


urlpatterns = [
    path("logout", logout_action, name="logout"), 
    path("login", login_action, name="login"),   

]       
