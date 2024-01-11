from django.shortcuts import render
from django.http import HttpResponse

def name(request, fname):
    return HttpResponse(f"<h1>Hello, {fname} HttpResponse</h1>")

