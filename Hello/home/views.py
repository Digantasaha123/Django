from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the Home Page 😍")

def about(request):
    return HttpResponse("About us ? 😒")

def services(request):
    return HttpResponse("What serveices do you want??👌🙌")

def contacts(request):
    return HttpResponse("Diganta15-4898@diu.edu.bd")
