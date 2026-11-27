from django.shortcuts import render
from .forms import ContactSellerForm

# Simple in-memory product list. Later you can move this into a database model.
PRODUCTS = [
    {'slug': 'toolbox', 'name': 'Heavy-Duty Steel Toolbox', 'price': 4999, 'old_price': 6499,
     'desc': '3-drawer rolling toolbox with lock. Great for any garage.', 'image': 'pages/img/toolbox.svg'},
    {'slug': 'socket-set', 'name': '150-Piece Socket Wrench Set', 'price': 3499, 'old_price': 4999,
     'desc': 'Chrome vanadium steel sockets with ratchet and carry case.', 'image': 'pages/img/socket.svg'},
    {'slug': 'floor-jack', 'name': '2-Ton Hydraulic Floor Jack', 'price': 5999, 'old_price': 7499,
     'desc': 'Low-profile jack with quick lift and safety valve.', 'image': 'pages/img/jack.svg'},
    {'slug': 'car-battery', 'name': 'Car Battery 12V 45Ah', 'price': 4299, 'old_price': 5199,
     'desc': 'Maintenance-free battery with 24-month warranty.', 'image': 'pages/img/battery.svg'},
    {'slug': 'alloy-wheels', 'name': '15" Alloy Wheel Set (4)', 'price': 18999, 'old_price': 23999,
     'desc': 'Lightweight alloy wheels, fits most hatchbacks and sedans.', 'image': 'pages/img/wheels.svg'},
    {'slug': 'work-light', 'name': 'LED Garage Work Light', 'price': 1299, 'old_price': 1799,
     'desc': 'Bright rechargeable LED light with magnetic stand.', 'image': 'pages/img/light.svg'},
]

for p in PRODUCTS:
    p['discount'] = round((p['old_price'] - p['price']) * 100 / p['old_price'])


def home(request):
    return render(request, 'pages/home.html', {'products': PRODUCTS})


def contact(request):
    choices = [(p['slug'], p['name']) for p in PRODUCTS]
    sent = False
    if request.method == 'POST':
        form = ContactSellerForm(request.POST, product_choices=choices)
        if form.is_valid():
            # In a real app you would save this or email the seller.
            print(form.cleaned_data)
            sent = True
            form = ContactSellerForm(product_choices=choices)
    else:
        selected = request.GET.get('product')
        initial = {'product': selected} if selected else {}
        form = ContactSellerForm(initial=initial, product_choices=choices)
    return render(request, 'pages/contact.html', {'form': form, 'sent': sent})
