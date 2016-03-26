from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^register/$', views.register_user),
    url(r'^login/$', login, {'template_name':'login.html'} ),
    url(r'^logout/$', logout,{'template_name':'logout.html'}),
    url(r'^$', views.index),
    url(r'^', views.to_index),
]