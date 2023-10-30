from django.urls import path
from credantials import views

urlpatterns = [

    path("log",views.Login,name="log"),
    path("reg",views.Register,name="reg"),
    path("logout",views.Logout,name="logout")
]
