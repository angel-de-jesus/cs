from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from . import views 

urlpatterns = [
    re_path(r'^$', views.AlumnoList.as_view()),
    re_path(r'^(?P<pk>\d+)$', views.AlumnoDetail.as_view()),

]
