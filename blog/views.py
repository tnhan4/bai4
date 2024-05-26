from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product

# Create your views here.
# products = [
#     {
#         'id': 1,
#         'name': 'TV',
#         'img': 'https://product.hstatic.net/200000574527/product/smart_tv_samsung_4k_qled_65_inch_qa65q63b_ec2a4bbcc6fb4e509c73069125c67844_1024x1024.jpg',
#         'description': 'Rõ nguồn gốc, hàng nhập khẩu, hiện đại, giá rẻ, màn hình 7inch to rộng',
#         'price': '50.000.000VND'
#     },
#     {
#         'id': 2,
#         'name': 'Laptop',
#         'img': 'https://m.media-amazon.com/images/S/aplus-media/vc/779be7f4-dbad-458a-bc30-f793cd214059.jpg',
#         'description': 'Nhẹ tay, kích cỡ vừa phải, có thể mang theo bên mình, giá sinh viên',
#         'price': '9.999.999VND'

#     },
#     {
#         'id': 3,
#         'name': 'PC',
#         'img': 'https://th.bing.com/th/id/R.a3fdb7a627c3917ee14cd1fa8675b81c?rik=ujf72NyBMs6%2bLA&riu=http%3a%2f%2fwww.techdaring.com%2fwp-content%2fuploads%2f2016%2f08%2fPC-Compatibility.jpg&ehk=JyKEjQ%2fgsY4ft7%2bqvfU9Y04Rjl49CHBbTWA8p75cE8M%3d&risl=&pid=ImgRaw&r=0',
#         'description': 'dùng để chiến mọi loại game nặng nhẹ khác nhau(bao gồm card đồ họa), bảo mật thông tin khá tốt',
#         'price': 'Đến cửa hàng để biết thêm chi tiết'
#     },
#     {
#         'id': 4,
#         'name': 'Samsung',
#         'img': 'https://th.bing.com/th/id/R.dab6b3d43d7a63b9cbfe3f4d92125746?rik=jndeBIifLU5%2b7g&pid=ImgRaw&r=0',
#         'description': 'Điện thoại samsung đời mới, có khả năng gập và cấu hình cao, chụp ảnh đẹp',
#         'price': '30.000.000VND'
#     },
#     {
#         'id': 5,
#         'name': 'Card đồ họa',
#         'img': 'https://th.bing.com/th/id/OIP.mDyD3FXWJihbwg3Y_uGjgAHaEo?rs=1&pid=ImgDetMain',
#         'description': 'Card xịn, chs dc elden ring , lol',
#         'price': '304.090.999VND'
#     },
#     {
#         'id': 6,
#         'name': 'Máy in',
#         'img': 'https://th.bing.com/th/id/OIP.tOz9MdoL9el1LyZK-gzTaQHaHa?rs=1&pid=ImgDetMain',
#         'description': 'Máy in chất lượng cao, in dc từ xa',
#         'price': '2.000.000VND'
#     },
#     {
#         'id': 7,
#         'name': 'Loa',
#         'img': 'https://th.bing.com/th/id/R.2382c35e150745a46defb719ea2a9683?rik=1jMCsN1xXQ6m6w&pid=ImgRaw&r=0',
#         'description': 'Loa nghe được tiếng chân',
#         'price': '1.490.000VND'
#     },
# ]

def home(req):
    products = Product.objects.all()
    return render(req, 'product.html', context={'products': products})

def product_detail(req, pk):
    product = Product.objects.get(pk=pk)
    # product = Product.objects.all(pk=pk)
    return render(req, 'product_detail.html', { 'product': product })