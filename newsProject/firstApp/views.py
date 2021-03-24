from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'firstApp/home.html')
def movie(request):
    return render(request,'firstApp/movies.html')
def politics(request):
    return render(request,'firstApp/politics.html')
def sports(request):
    return render(request,'firstApp/sports.html')
