from django.test import TestCase # type: ignore
from .models import YourModel  # Replace with your actual model

class YourModelTestCase(TestCase):
    def setUp(self):
        # Set up any initial data for your tests here
        YourModel.objects.create(name="Test Name", value=42)

    def test_model_creation(self):
        """Test that the model was created successfully."""
        obj = YourModel.objects.get(name="Test Name")
        self.assertEqual(obj.value, 42)

    def test_model_string_representation(self):
        """Test the string representation of the model."""
        obj = YourModel.objects.get(name="Test Name")
        self.assertEqual(str(obj), "Expected String Representation")  # Replace with expected output