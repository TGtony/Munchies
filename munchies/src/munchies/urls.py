from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import search.urls
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^search/', include(search.urls, namespace='search')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)