from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def take_homepage(request):
    return render(request, 'catalog/take_homepage.html')

def take_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'пользватель {name} , телефон {phone}, говорит {message}')

    return render(request, 'catalog/take_contact.html')

def product_card(request):
    context = {
        'product_card' : Product.objects.all()
    }
    return render(request, 'catalog/product_card.html', context)