from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html', {})  # Create a simple home page