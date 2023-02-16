from django.shortcuts import render
from .models import Pizza, Toppings
# Create your views here.
def index(request):
    return render(request, 'pizzerias/index.html')

def pizza(request):
    pizzas = Pizza.objects.order_by("name")
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizza.html', context)