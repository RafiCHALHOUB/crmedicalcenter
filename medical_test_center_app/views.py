from django.http import HttpResponse
from medical_test_center_app.models import *
from django.shortcuts import render, redirect
from medical_test_center_app.models import Test
from django.views import View
from .forms import MedicalApplicationForm
from django.contrib.auth import logout
from medical_test_center_app.models import Patient
def homepage(request,):
    return render(request, "homepage.html")


def tests(request,):
    return render(request, "tests.html", {"Tests": Test.objects.all()})
def patients(request,):
    return render(request, "patients.html", {"Patients": Patient.objects.all()})


def biologists(request,):
    return render(request, "team.html", {"Biologists": Biologist.objects.all()})


def display_biologist(request, biologistid):
    biologist =Biologist.objects.filter(ID_bio=biologistid)
    if len(biologist)==1:
        biologist = biologist[0]
        return render(request, "biologist.html",{"biologist" : biologist})
    else:
        return HttpResponse("Error")

def logoutview(request):
    logout(request)
    # Redirect to the homepage.
    return redirect('/')  # Replace 'home' with the name of your homepage URL pattern.


class MedicalApplicationFormView(View):
    template_name = 'medical_form.html'

    def get(self, request, *args, **kwargs):
        form = MedicalApplicationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MedicalApplicationForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            patient = form.save()  # This saves the form data and returns the Patient instance
            # You can do additional processing with the patient instance if needed
            # For example, you can print the patient ID
            print(f"New patient ID: {patient.ID_patient}")

            # Redirect to the same page or any other page you want
            return redirect('medical_application_form')

        # If the form is not valid, display the form with errors
        return render(request, self.template_name, {'form': form})

