from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from website.views import register, account_activation_sent, activate
from website.forms import UserForm
from website.views import *
from . import views
urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<category_id>[0-9]+)/$',views.details,name='details'),
    url(r'^accounts/register/$',views.register, name='register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^registration/', include('registration.auth_urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.login, name='logout'),
    
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^activation_complete/$', views.activation_complete, name='activation_complete')
]
