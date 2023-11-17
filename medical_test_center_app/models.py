from decimal import Decimal

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class Patient(models.Model):
    """
    Model representing a patient in the medical system.
    """

    # Field choices for gender
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    # Primary key for Patient model
    ID_patient = models.AutoField(primary_key=True)

    # Patient details
    firstname_patient = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z ]*$', message='Only letters and spaces are allowed.')])
    lastname_patient = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z ]*$', message='Only letters and spaces are allowed.')])
    street_number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)]
    )
    street_name = models.CharField(max_length=50)
    postal_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(r'^\d{5}$', message='Postal code must be 5 digits')]
    )
    city_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_nb = models.PositiveIntegerField()
    birth_date = models.DateField()
    insured = models.IntegerField(choices=[(0, 'Not Insured'), (1, 'Insured')])

    # Method to check if the patient is insured
    def is_insured(self):
        return self.insured == 1

    is_insured.boolean = True  # This is used to display a nice True/False icon in the admin

    def __str__(self):
        return f"{self.firstname_patient} {self.lastname_patient}"

class Biologist(models.Model):
    """
    Model representing a biologist in the medical system.
    """

    # Primary key for Biologist model
    ID_bio = models.AutoField(primary_key=True)

    # Biologist details
    firstname_bio = models.CharField(max_length=255)
    lastname_bio = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname_bio} {self.lastname_bio}"

class Test(models.Model):
    """
    Model representing a medical test in the system.
    """

    # Primary key for Test model
    ID_test = models.AutoField(primary_key=True)

    # Foreign key linking Test to Biologist
    ID_bio = models.ForeignKey(Biologist, on_delete=models.CASCADE)

    # Test details
    name_test = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('ID_test', 'ID_bio')

class Performed(models.Model):
    """
    Model representing a performed medical test for a patient.
    """

    # Foreign keys linking Performed to Patient and Test
    ID_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ID_test = models.ForeignKey(Test, on_delete=models.CASCADE)

    # Performed test details
    description_results = models.CharField(max_length=255)
    date_results = models.DateField()

    class Meta:
        unique_together = ('ID_patient', 'ID_test')

    def __str__(self):
        return f"Performed Test for {self.ID_patient} - Test: {self.ID_test}"

class Bill(models.Model):
    """
    Model representing a bill for a patient.
    """

    # Primary key for Bill model
    ID_bill = models.AutoField(primary_key=True)

    # Foreign key linking Bill to Patient
    ID_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Bill details
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_red = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('ID_bill', 'ID_patient')

    def __str__(self):
        return f"Bill {self.ID_bill} for Patient {self.ID_patient}"

class Associate(models.Model):
    """
    Model representing an association between a bill and a test.
    """

    # Foreign keys linking Associate to Bill and Test
    ID_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    ID_test = models.ForeignKey(Test, on_delete=models.CASCADE)

    # Association details
    date_test = models.DateField()
    date_bill = models.DateField()

    class Meta:
        unique_together = ('ID_bill', 'ID_test')

    def __str__(self):
        return f"Association of Bill {self.ID_bill} and Test {self.ID_test}"
