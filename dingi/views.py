from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("<center><h1>Welcome to Homepage</h1></center>")
def intro(request):
    return HttpResponse("<marquee><h1>Hello Macha.........How are you!!</h1></marquee>")
def mypage(request):
    return render(request,'intro.html')