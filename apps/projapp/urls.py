from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^login_process$', views.login_process),
    url(r'^register$', views.register),
    url(r'^register_process$', views.register_process),
    url(r'^success$', views.success),
    url(r'^create_product$', views.create),
    url(r'^menshirt$', views.men_shirt),
    url(r'^women-vneck$', views.women_vneck),
    url(r'^women-tshirt$', views.women_tshirt),
    url(r'^sunglass$', views.sunglass),
    url(r'^backpack$', views.backpack),
    url(r'^jacket$', views.jacket),
]