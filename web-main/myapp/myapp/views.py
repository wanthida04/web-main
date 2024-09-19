from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def calorie(request):
    return render(request, 'calorie.html')

def about(request):
    return render(request, 'about.html')

def detail1(request):
    return render(request, 'detail1.html')

def detail2(request):
    return render(request, 'detail2.html')

def detail3(request):
    return render(request, 'detail3.html')