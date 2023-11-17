from django import forms
from .models import Patient

class MedicalApplicationForm(forms.ModelForm):
    """
    Form for medical applications, based on the Patient model.
    """

    # Customizing the birth_date field to use a date picker in the form
    birth_date = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Patient

        # Exclude the 'ID_patient' field from the form (auto-generated primary key)
        exclude = ['ID_patient']

        # Custom labels for form fields
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
