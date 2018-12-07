from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
     url(r'^$', views.inicio, name="paginaprincipal"),
     url('trabajadores/inicio', views.redirigir, name="redirigir"),
     url('trabajadores/login', views.login , name="login"),
]
