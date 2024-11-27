from django.forms import ModelForm

from .models import *


class Login_form(ModelForm):
    class Meta:
        model = Login_model
        fields = ['username', 'password']

class AddDoctor_form(ModelForm):
    class Meta:
        model = Doctor_model
        fields = ['Firstname', 'Lastname', 'Phone', 'Email', 'Qualification', 'Year_of_experience', 'Department']

class AddPost_from(ModelForm):
    class Meta:
        model = Post_model
        fields = ['Image', 'Description']

class RegisterPharmacist_form(ModelForm):
    class Meta:
        model = Pharmacist_model
        fields = ['Firstname', 'Lastname', 'Address', 'Phone', 'Email', 'Pharmacy_Name']

class AddMedicine_form(ModelForm):
    class Meta:
        model = Medicine_model
        fields = ['Medicine_Name', 'Quantity', 'price', 'Description', 'Status']