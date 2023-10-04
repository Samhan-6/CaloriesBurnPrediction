from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="User Name.")
    gender = models.CharField(
        max_length=10)
    date_of_birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    country = models.CharField(
        max_length=50,
        help_text="The country you currently living.")
    email = models.EmailField(
        help_text="The contact email of the user.")
    password = models.CharField(
        max_length=50,
        help_text="Create a new password.")

    def __str__(self):
        return self.name