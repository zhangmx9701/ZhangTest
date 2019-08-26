from django.urls import path
from userapp import views

app_name = "user"

urlpatterns = [
    path('registlogic/',views.registlogic,name="registlogic"),
    path('login/',views.login,name="login"),
    path('loginlogic/',views.loginlogic,name="loginlogic"),
    path('getcaptcha/',views.getcaptcha,name="getcaptcha"),
    path('usercheck/',views.usercheck,name="usercheck"),
    path('numcheck/',views.numcheck,name="numcheck"),
]