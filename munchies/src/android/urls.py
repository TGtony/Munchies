from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<vec>[0-3]+)/$', views.androidQuery, name='androidQuery'),

]
