from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요! 승범이의 나라에 오신 것을 환영합니다")