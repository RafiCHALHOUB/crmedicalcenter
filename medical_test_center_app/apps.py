from django.apps import AppConfig

class MedicalTestCenterAppConfig(AppConfig):
    """
    Configuration class for the 'medical_test_center_app' Django app.
    """

    # Use 'django.db.models.BigAutoField' as the default auto field for this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the app
    name = 'medical_test_center_app'
