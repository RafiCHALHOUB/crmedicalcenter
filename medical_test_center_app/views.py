from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import View
from .models import Test, Patient, Biologist
from .forms import MedicalApplicationForm

def homepage(request):
    """
    Render the homepage.
    """
    return render(request, "homepage.html")

def tests(request):
    """
    Render the tests page with all available tests.
    """
    return render(request, "tests.html", {"Tests": Test.objects.all()})

def patients(request):
    """
    Render the patients page with all available patients.
    """
    return render(request, "patients.html", {"Patients": Patient.objects.all()})

def biologists(request):
    """
    Render the team page with all available biologists.
    """
    return render(request, "team.html", {"Biologists": Biologist.objects.all()})

def display_biologist(request, biologistid):
    """
    Display information about a specific biologist.
    """
    biologist = Biologist.objects.filter(ID_bio=biologistid)
    if len(biologist) == 1:
        biologist = biologist[0]
        return render(request, "biologist.html", {"biologist": biologist})
    else:
        # If there is an issue with the biologist ID, return an error response
        return HttpResponse("Error")

def logoutview(request):
    """
    Logout the user and redirect to the homepage.
    """
    logout(request)
    return redirect('/')
class MedicalApplicationFormView(View):
    """
    View for handling medical application form submissions.
    """
    template_name = 'medical_form.html'
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests for the medical application form view.
        """
        form = MedicalApplicationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for the medical application form view.
        """
        form = MedicalApplicationForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            patient = form.save()  # This saves the form data and returns the Patient instance
            # Additional processing with the patient instance if needed
            print(f"New patient ID: {patient.ID_patient}")



            # Redirect to the same page or any other page you want
            return redirect('medical_application_form')
        # If the form is not valid, display the form with errors
        return render(request, self.template_name, {'form': form})
