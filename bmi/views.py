from django.shortcuts import render

# Create your views here.
# CRUD-L
# : Create, Read, Update, Delete, List
# 함수형 뷰: 문법적 형식이 함수 - 제네릭 뷰가 없거나 직접 기능을 커스터마이징하고 싶을 떄 사용
# 클래스형 뷰: 문법적 형식이 클래스 - 웹서비스 영역에서 빈번하게 만드는 기능은 제네렉 뷰가 이미 있어서,
#  이를 상속받을 때 클래스형 뷰를 사용


from django.views.generic.list import ListView
from .models import BMI

# 제네릭 뷰 = 모델베이스 뷰(모델에 대한 조작을 가하므로)


class BMIList(ListView):
    model = BMI


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class BMIDetail(DetailView):
    model = BMI


class BMICreate(CreateView):
    model = BMI
    fields = ['weight', 'height']
    success_url = '/'


class BMIUpdate(UpdateView):
    model = BMI
    fields = ['weight', 'height']
    success_url = '/'


class BMIDelete(DeleteView):
    model = BMI
    success_url = '/'

