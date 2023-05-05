from django.shortcuts import render

# Create your views here.
def take_homepage(request):
    return render(request, 'catalog/take_homepage.html')

def take_contact(request):
    return render(request, 'catalog/take_contact.html')