from django.conf.urls import url
from api import views
#template taggibg
app_name = 'api'


urlpatterns=[
        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),
        url(r'^aboutus/$',views.aboutus,name='aboutus'),
]
