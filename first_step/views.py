from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def test(request):
    return render(request, 'test.html')   


def base(request):
    return render(request, 'base.html')   