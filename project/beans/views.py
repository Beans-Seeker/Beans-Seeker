from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "main.html")

def cafes(request):
    return render(request, 'cafes.html')

def profile(request):
    return render(request, 'profile.html')