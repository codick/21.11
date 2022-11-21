from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(req, name, age, hobbies):
    return HttpResponse({name: name, age: age, hobbies: hobbies})


def about(req, from_where, school, love):
    return HttpResponse({from_where, ' ', school, ' ', love})


def contacts(req, github, telegram):
    return HttpResponse({github, ' ', telegram})
