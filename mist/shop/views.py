from django.shortcuts import render
from django.http import HttpResponse

# TEST
def index(requests):
    return HttpResponse('Hello')
