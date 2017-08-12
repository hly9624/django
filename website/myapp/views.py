# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.template import loader
import time
from myapp.models import *
from django.db.models import F,Q
import datetime
# Create your views here.

def global_setting(request):
    NAME = 'cainiao'
    TEL = '13888888888'
    GEYAN = '山有木兮木有枝，心悦君兮君不知'


    return locals()


def first(request):
     return HttpResponse("my first app")

def fun():
    return "hello"

class A(object):
    a = "clsaa->a"
    def f(self):
        return "jest a A:fun"

def bs(request):
    #方法一
    t = loader.get_template('bs.html')
    html = t.render({})
    return HttpResponse(html)

def test(request):
    return render(request,'bs.html',{})



def temp(request):
    #方法二
    #return render_to_response('bs.html',{})
    t = time.localtime()
    #方法三
    return render(request,'time.html',{'datetime':t})

def display_meta(request):
    num = 1
    s = "hello"
    l = [1,2,'c','nihao']
    t = [4,5,'d','tuple']
    d = {'a':'one','b':'two','c':'three'}
    f = fun()
    obj = A()

    return render(request,'meta.html',\
    {'num':num,'s':s,'list':l,'tuple':t,'dict':d,'fun':f,'obj':obj})


def tag(request):
    error = "error"
    l = [1,2,3,4]
    return render(request,'tags.html',{error:"a",'list':l})

def fil(request):
    num = 1
    s = "HELLO WORLD"

    return render(request,'filter.html',{'num':num,'s':s})

def base(request):
    return render(request,'extend.html',{})

def nav(request):
    return render(request,'nav.html',{})

def load(request):
    return render(request,'static.html',{})


def mydb(request):
    #增1
    # Author.objects.create(first_name = 'Jame',last_name = "Green",email = 'jm@123.com')
    # Publisher.objects.create(name = "人民",address = "beijing",city = "beijing",state_province = "haidian",country = "China",website = 'http://192.186.0.133')

    # Book.objects.create(title = "Python Book",publication_date=datetime.datetime.now(),publisher_id = 1)
    # Book.objects.create(title = "HTML5",publication_date=datetime.datetime.now(),publisher_id = 1)
    # Book.objects.create(title = "JavaScript",publication_date=datetime.datetime.now(),publisher_id = 1)

    # 增2
    # obj = Author(first_name = 'Han',last_name = "mei",email = 'hm@123.com')
    # obj.save()
    # dic = {'first_name' : 'Lei','last_name' : "li",'email' : 'll@123.com'}
    # obj = Author(**dic)
    # obj.save()

    #删
    # Author.objects.filter(id__gt=4).delete()


    #改1
    # Author.objects.filter(id=4).update(first_name = "lili")

    #改2
    # obj = Author.objects.get(id = 2)
    # obj.first_name = "lucy"
    # obj.save()

    #查 select * from author

    # a = Author.objects.all() # 每一条记录生成一个对象
    # b = Author.objects.all().values('email') # 取出所有记录的指定字段
    # c = Author.objects.all().values_list('first_name','email') # 取出所有记录的指定字段
    # d = Author.objects.get(id = 2)   # 获取某一记录的对象
    # e = Author.objects.filter(id = 1) #获取某一记录的对象列表

    # Author.objects.filter().update(age = F('age') + 1)
    #
    # q = Q()
    # print dir(q)
    #
    # q.connector = 'AND'
    # q.children.append(('id',3))
    # q.children.append(('last_name','mei'))
    #
    # f = Author.objects.filter(q)

    return HttpResponse("OK")

def mtm(request):
    book1 = Book.objects.get(id = 2)
    s = book1.publisher.name

    pub1 = Publisher.objects.get(id = 1)
    book_list = pub1.book_set.all()

    author_list = book1.author.all()

    # count = Book.myobjects.title_count('HTML5')

    book2_list = Book.myobjects.all().little()

    return HttpResponse(book2_list)



def postImage(request):
    return render(request,'image.html',{})

def message(request):
    try:
        img = Ad(title = "imgTest",img = request.FILES.get('picfile'))
        img.save()
    except Exception,e:
        return HttpResponse("Error:%s"%e)
    return HttpResponse("post images")
