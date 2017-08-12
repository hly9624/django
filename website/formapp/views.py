# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from formapp.forms import *
from myapp.models import Book,Author


# Create your views here.

def search_form(request):
    return render(request,'search_form.html',{})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return HttpResponse("I have get the '%s'"%q)
    else:
        return render(request,'search_form.html',{'error':True})
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')

        if not request.POST.get('email',''):
            errors.append('Enter a email address')

        if not request.POST.get('message',''):
            errors.append('Enter a message')

        if not errors:
            return HttpResponseRedirect("/form/contact/thanks")
    return render(request,"contact_form.html",{'errors':errors,'subject':request.POST.get('subject'),'email':request.POST.get('email'),'message':request.POST.get('message')})
def thanks(request):
    return HttpResponse("Thanks,we have get your message")


def formtest(request):
    # return render(request,'formset.html',{})
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['subject']
            print cd['mail']
            print cd['topic']
            print cd['message']
            print cd['cc_myself']
            return HttpResponseRedirect('/form/form')
    else:
        form = RemarkForm()

        return render(request,'formset.html',{'form':form})


def bookset(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            dic = {'first_name':cd['first_name'],'last_name':cd['last_name'],'age':cd['age'],'email':cd['email']}
            Author.objects.create(**dic)
            return HttpResponseRedirect('/form/bookform')
    else:
        form = AuthorForm()

    return render(request,'bookset.html',{'form':form})
