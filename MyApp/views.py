from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):

    return render(request,'MyApp/home.html')

def Projects(request):

    return render(request,'MyApp/projects.html')

def Education(request):

    return render(request,'MyApp/education.html')

def Work_Experience(request):

    return render(request,'MyApp/work_experience.html')

def blog(request):

    return HttpResponse('Aqui va un blog, hagale la plantilla')
