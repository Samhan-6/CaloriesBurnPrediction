from django.test import TestCase
from contact.models import Contact


class TestModel(TestCase):
    def test_create_contact(self):
        # Create a Contact instance
        contact = Contact(
            email="test@example.com",
            subject="Test Subject",
            message="Test Message"
        )
        contact.save()

        # Check if the contact was saved to the database
        saved_contact = Contact.objects.get(email="test@example.com")
        self.assertEqual(saved_contact.subject, "Test Subject")
        self.assertEqual(saved_contact.message, "Test Message")

    def test_str_method(self):
        # Create a Contact instance
        contact = Contact(
            email="test@example.com",
            subject="Test Subject",
            message="Test Message"
        )

        # Check the string representation of the contact
        self.assertEqual(str(contact), "test@example.com")