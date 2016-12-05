from django.conf.urls import url
from .import views

app_name = 'contact'

urlpatterns = [

    # /contact/
    url(r'^$', views.ContactUs.as_view(), name='index'),

    # /contact/html/
    url(r'^html/$', views.ContactUs.as_view(), name='html'),

]