from django.db import models

# Create your models here.

class Login_model(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

class Patient_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class Doctor_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Year_of_experience = models.CharField(max_length=100, null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True)

class Pharmacist_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Pharmacy_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

class Booking_model(models.Model):
    PATIENT_ID = models.ForeignKey(Patient_model, on_delete=models.CASCADE)
    DOCTOR_ID = models.ForeignKey(Doctor_model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post_model(models.Model):
    Image = models.FileField(upload_to='post/', null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)

class DeliveryBoy_model(models.Model):
    LOGIN_ID = models.ForeignKey(Login_model, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100, null=True, blank=True)
    Lastname = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Address = models.CharField(null=True, blank=True, max_length=100)

class Medicine_model(models.Model):
    Medicine_Name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField( null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True) 
    Status = models.CharField(max_length=100, null=True, blank=True)

class Prescription_model(models.Model):
    DOCTOR_ID = models.ForeignKey(Doctor_model, on_delete=models.CASCADE)
    PATIENT_ID = models.ForeignKey(Patient_model, on_delete=models.CASCADE)
    Prescription = models.CharField(max_length=100, null=True, blank=True)
    MEDICINE_ID = models.ForeignKey(Medicine_model, on_delete=models.CASCADE)

class Medicine_booking(models.Model):
    PATIENT_ID = models.ForeignKey(Patient_model, on_delete=models.CASCADE)
    PHARMACY_ID = models.ForeignKey(Pharmacist_model, on_delete=models.CASCADE)
    PRESCRIPTION_ID = models.ForeignKey(Prescription_model, on_delete=models.CASCADE)
    Delivery_Type = models.CharField(max_length=100, blank=True, null=True)
    DELIVERYBOY_ID = models.ForeignKey(DeliveryBoy_model, on_delete=models.CASCADE)