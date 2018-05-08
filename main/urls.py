from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^$', views.Main.as_view(), name='quiz_main'),
    url(r'^leader/$', views.leader, name='leader'),
    url(r'^result/$', views.result, name='result'),
]