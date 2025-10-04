from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def home_page_view(request):
    return HttpResponse("This will be the homepage for my website shopmajuu/green shippers")
