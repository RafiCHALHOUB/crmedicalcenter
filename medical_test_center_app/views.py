from django.http import HttpResponse
from medical_test_center_app.models import *
from django.shortcuts import render, redirect
from medical_test_center_app.models import Test
from django.views import View
from .forms import MedicalApplicationForm  # Import your form class
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
            # Redirect to a success page or homepage
            return redirect('homepage')
        return render(request, self.template_name, {'form': form})

