from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def example(requests):
    return HttpResponse("Чё зашёл, тут пусто")


