from django.conf.urls import url
from . import views
app_name = "booktest"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^about/$',views.about,name='about'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),

]