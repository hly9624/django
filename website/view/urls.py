#coding=utf-8


from django.conf.urls import url
from view.views import *
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView #跳转

urlpatterns = [
    url(r'^test/(\d{1,2})/$',test),
    url(r'foo/$',foo_bar,{'template_name':"foo.html"}),
    url(r'bar/$',foo_bar,{'template_name':"bar.html"}),
]

urlpatterns += [
    url(r'^about/$',TemplateView.as_view(template_name = 'about.html')),
    url(r'^go-to',RedirectView.as_view(url='/view/about/')),#跳转内网外网都可以
    url(r'^my_view',MyView.as_view()),
]
