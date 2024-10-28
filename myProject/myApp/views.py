from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'myApp/home.html')
def pendidikan (request):
    return render(request, 'myApp/pendidikan.html')
def pengalaman_hidup (request):
    return render(request, 'myApp/pengalaman_hidup.html')
def sosial_media (request):
    return render(request, 'myApp/sosial_media.html')