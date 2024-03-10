from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello")
def home(request):
    return render(request, 'index.html')
def col(request):
    return render(request, "col.html")