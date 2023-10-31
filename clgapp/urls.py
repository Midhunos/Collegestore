

from django.urls import path
from clgapp import views


urlpatterns = [
  
    path("",views.index,name="index"),
    path("index2",views.index2,name="index2"),
    path("order_form",views.order_form,name="order_form"),
    path("load_courses",views.load_courses,name="load_courses")



]
