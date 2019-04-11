from  django.conf.urls import url


from .import views,viewserializer
from .viewserializer import InformationApiView
urlpatterns=[

    url(r'^home/$',views.homeviews,name="homeviews"),
    url(r'^home/(?P<userid>\d+)/$',views.tempviews,name="tempviews"),
    #url(r'^home/catalog/(?P<userid>\d+)/(?P<catid>\d+)/$', views.catalogviews, name="catalogviews"),
    url(r'^login/$',views.LoginViews,name="LoginViews"),
    url(r'^register/$',views.registerviews,name="registerviews"),
    url(r'^logout/$',views.DoLogout,name="DoLogout"),

    url(r'^home/catalog/(?P<userid>\d+)/(?P<catid>\d+)/$',views.testings,name="testings"),
    url(r'^questions/$', views.questions, name="questions"),
    url(r'^home/information/(?P<userid>\d+)/(?P<catid>\d+)/$', views.information, name="information"),

    url(r'^home/api/(?P<id>\d+)/$', viewserializer.InformationApiView.as_view(), name="informationApiview"),
    url(r'^home/qu/api/(?P<id>\d+)/$', viewserializer.QuestionApiView.as_view(), name="QuestionApiview"),
    url(r'^home/single/api/(?P<id1>\d+)/(?P<id2>\d+)/$',viewserializer.SingleContentView.as_view(),name="SingleContentView"),
    url(r'^playit/$', views.playit, name="playit"),

]