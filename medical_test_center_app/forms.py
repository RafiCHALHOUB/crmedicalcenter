from django import forms
from .models import Patient


class MedicalApplicationForm(forms.ModelForm):
    birth_date = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Patient
        exclude = ['ID_patient']
        labels = {
            'firstname_patient': 'First Name',
            'lastname_patient': 'Last Name',
            'gender': 'Gender',
            'insured': 'Insurance Status',
            'street_number': 'Street Number',
            'street_name': 'Street Name',
            'postal_code': 'Postal Code',
            'city_name': 'City',
            'phone_nb': 'Phone Number',
        }
