from django.shortcuts import redirect, render
from app.models import slider, BannerAreas

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    sliders = slider.objects.all()
    banners = BannerAreas.objects.all()
    context = {
        'sliders':sliders,
        'banners':banners
        }
    return render(request, 'main/home.html',context)

