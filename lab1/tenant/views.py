from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def tenant_list(request):
    return render(request, 'tenant/index.html')