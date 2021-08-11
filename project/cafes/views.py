from django.shortcuts import render

# Create your views here.

def cafes(request):
    return render(request, "cafes.html")
    
def tomntoms(request):
    return render(request, "tomntoms.html")

def starbucks(request):
    return render(request, 'starbucks.html')
