from django.shortcuts import render

# Create your views here.

def food(request):
    return render(request,'Food Delveary.html')

def instagram2(request):
    return render(request,'instagram2.html')

def new(request):
    return render(request,'new.html')

def task(request):
    return render(request,'task.html')
def google(request):
    return render(request,'google.html')


def output(request):
    return render(request,'instagram.html')


    

    