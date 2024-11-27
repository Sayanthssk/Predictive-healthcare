
from django.urls import path

from .views import *

urlpatterns = [
    path('index', Index_page.as_view(), name='index'),
    path('adddoctor', Adddoctor.as_view(), name='adddoctor'),
    path('addmedicine', Addmedicine.as_view(), name='addmedicine'),
    path('addpost', Addpost.as_view(), name='addpost'),
    path('addprescription', Addprescription.as_view(), name='addprescription'),
    path('editdoctor/<int:pk>', Editdoctor.as_view(), name='editdoctor'),
    path('deletedoctor/<int:pk>', DeleteDoctor.as_view(), name='deletedoctor'),
    path('editmedicine/<int:pk>', EditMedicine.as_view(), name='editmedicine'),
    path('deletemedicine/<int:pk>', DeleteMedicine.as_view(), name='editmedicine'),
    path('editpharmacy/<int:pk>', EditPharmacy.as_view(), name='editpharmacy'),
    path('deletepharmacy/<int:pk>', DeletePharmacy.as_view(), name='deletpharmacy'),
    path('editpost', EditPost.as_view(), name='editpost'),
    path('login/', Login.as_view(), name='login'),
    path('registerpharmacist', RegisterPharmacist.as_view(), name='registerpharmacist'),
    path('viewbooking', ViewBooking.as_view(), name='viewbooking'),
    path('viewdoctors', ViewDoctors.as_view(), name='viewdoctors'),
    path('viewmedicine', ViewMedicines.as_view(), name='viewmedicine'),
    path('viewmedicinedoc', ViewMedicineDoc.as_view(), name='viewmedicinedoc'),
    path('viewpharmacy', ViewPharmacy.as_view(), name='viewpharmacy'),
    path('viewpost', ViewPost.as_view(), name='viewpost'),
    path('viewprescription', ViewPrescription.as_view(), name='viewprescription'),
    path('adminhome', AdminHome.as_view(), name='adminhome'),
    path('viewpatient', View_patient.as_view(), name='viewpatient')

]
