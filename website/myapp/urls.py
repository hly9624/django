#coding=utf-8

from django.conf.urls import url
from myapp.views import *

urlpatterns = [
    url(r'^first/$',first),
    url(r'^bs/$',bs),
    url(r'^test/$',test),
    url(r'^template',temp),
    url(r'^meta/$',display_meta),
    url(r'^haha/$',tag),
    url(r'^filter/$',fil),
    url(r'^extend/$',base,name='base'),
    url(r'^nav/$',nav),
    url(r'^static/$',load),

]

urlpatterns += [
    url(r'^models/$',mydb),
    url(r'^models1/$',mtm),
]
