from django.conf.urls import url
from django.contrib import admin

from hello import views

urlpatterns = [
    url(r'^$', views.hello, {'a': 11111}),
    url(r'^test/(?P<id>\d{2})/(?P<key>\w+)/$', views.test),
    url(r'^add_publisher/', views.add_publisher, name="add_publisher"),

]
