from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    peoples =[
        {'name' : 'Diganta', 'age' : 11,'leisure' : 'Music production' },
        {'name' : 'Mostakem', 'age' : 28,'leisure' : 'Coding' },
        {'name' : 'Chayon', 'age' : 12,'leisure' : 'Bhojpuri song' },
        {'name' : 'Nafian', 'age' : 29,'leisure' : 'Luicchami' },
    ]
    #context use kore amra backend theke data fetch kori 
    return render(request, 'index.html', context = {'peoples': peoples})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey this is a success page<h1>")