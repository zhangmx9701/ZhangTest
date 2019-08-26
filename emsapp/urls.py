from django.urls import path
from emsapp import views

app_name = "ems"

urlpatterns = [
    path('main/',views.main,name="main"),
    path('addstatus/',views.addstatus,name="addstatus"),
    path('update/',views.update,name="update"),
    path('loadupdate/',views.loadupdate,name="loadupdate"),
    path('updatestatus/',views.updatestatus,name="updatestatus"),
    path('delete/',views.delete,name="delete"),
    path('forcelogin/',views.forcelogin,name="forcelogin"),
]