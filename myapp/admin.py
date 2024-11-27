from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Login_model)
admin.site.register(Patient_model)
admin.site.register(Doctor_model)
admin.site.register(Pharmacist_model)
admin.site.register(Booking_model)
admin.site.register(Post_model)
admin.site.register(DeliveryBoy_model)
admin.site.register(Medicine_model)
admin.site.register(Prescription_model)
admin.site.register(Medicine_booking)