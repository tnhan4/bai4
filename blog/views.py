from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello")
def home(request):
    return render(request, 'index.html')
def demo(req):
    data = [
        {
        'name': 'Trọng Nhân',
        'age': 20
        }
    ]
    return JsonResponse(data, safe=False)
def product(req):
    data = [
        {
            'name': 'Đăng Hán',
            'born': '2003'
        },
        {
            'name': 'Văn Tiến',
            'born': '2003',
        }
    ]
    return render(req, 'pages/product.html', {'products': data})