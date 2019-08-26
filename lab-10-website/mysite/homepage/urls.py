from django.conf.urls import url

from . import views
from django.contrib.auth.views import login,logout

#app_name = 'home'

urlpatterns = [
    # ex: /homepage/
    url(r'^$', views.home),
    url(r'^login/$',login,{'template_name':'homepage/login.html'}),
    url(r'^sreg/$',login,{'template_name':'homepage/successreg.html'}),
    url(r'^register/$',views.register),
    url(r'^logout/$',logout,{'template_name':'homepage/logout.html'}, name='logout'),
    url(r'^loginhome/$',views.loginhome),
    url(r'^total/$',views.total)
]
