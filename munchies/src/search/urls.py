from django.conf.urls import url
from .views import SearchView
from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$', SearchView.as_view(), name='tag_search'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^random/$', views.random, name='random'),
    url(r'^results/$', views.results, name='results'),
    url(r'^android/(?P<adjs>[0-2]+)/$', views.androidQuery, name='androidQuery'),
    url(r'^query/(?P<asin>[ \w+]+)/$', views.asinQry, name='asinQry'),
]
