from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')
    #return HttpResponse('Index blog')
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("We are contact")
def tracker(request):
    return HttpResponse("We are tracker")
def search(request):
    return HttpResponse("We are search")
def productview(request):
    return HttpResponse("We are productview")
def checkout(request):
    return HttpResponse("We are checkout")