from django.shortcuts import render
def home(request):
    return render(request,'indexform.html')
def page2(request):
    return render(request,'page2.html')
def newhtml(request):
    return render(request,'newhtml.html')