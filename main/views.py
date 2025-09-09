from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'shop_name' : 'Garuda Football Shop',
        'name': 'Haris Azzahra Lunaya',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)