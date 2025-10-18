from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

def display(request):
    if request.method == 'POST':
        return HttpResponse("This page displays order, tracking, issues and returns")
    elif request.method == 'GET':
        return HttpResponse("Please submit a form to view order, tracking, issues, and returns.")
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

