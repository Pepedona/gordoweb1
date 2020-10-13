from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for gordolab"""
    return render(request, 'gordolab/index.html')

def gordofut(request):
    """Home page for gordofut"""
    return render(request, 'gordolab/gordofut.html')

def quienessomos(request):
    """information about us"""
    return render(request, 'gordolab/quienessomos.html')