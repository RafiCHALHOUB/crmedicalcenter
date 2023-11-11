from django.http import HttpResponse
from django.shortcuts import render
from medical_test_center_app.models import *
from django.shortcuts import render, redirect
from .models import Bill
from django.core.management.base import BaseCommand
from medical_test_center_app.models import Test
# Create your views here.
def homepage(request,):
    return render(request, "homepage.html")


def tests(request,):
    return render(request, "tests.html", {"Tests": Test.objects.all()})


def biologists(request,):
    return render(request, "team.html", {"Biologists": Biologist.objects.all()})

def biologist(request,):

    return render(request, "biologist.html", {"Biologist": Biologist.objects.all()})


def display_biologist(request, biologistid):
    biologist =Biologist.objects.filter(ID_bio=biologistid)
    if len(biologist)==1:
        biologist = biologist[0]
        return render(request, "biologist.html",{"biologist" : biologist})
    else:
        return HttpResponse("Error")