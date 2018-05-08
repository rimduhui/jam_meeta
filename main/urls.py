from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Main.as_view(), name='quiz_main'),

    url(r'^result/$', views.result, name='result'),
]