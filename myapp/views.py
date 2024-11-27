from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

class Index_page(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Adddoctor(View):
    def get(self, request):
        return render(request, 'adddoctor.html')
        
    def post(self, request):
        form = AddDoctor_form(request.POST)
        if form.is_valid():
            try:
                doctor = form.save(commit=False)
                doctor.LOGIN_ID = Login_model.objects.create(username=request.POST['username'], password=request.POST['password'], type='doctor', status='active')
                doctor.LOGIN_ID.save()
                doctor.save()
                return redirect('viewdoctors')  
            except Login_model.DoesNotExist:
                form.add_error(None, "Associated login account does not exist.")
        return render(request, 'adddoctor.html', {'form': form})
    
    
class Addmedicine(View):
    def get(self, request):
        return render(request, 'addmedicine.html')
    def post(self, request):
        c = AddMedicine_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('viewmedicine')
    

    
class Addpost(View):
    def get(self, request):
        return render(request, 'addpost.html')
    def post(self, request):
        c = AddPost_from(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            return redirect('addpost')
    
class Addprescription(View):
    def get(self, request):
        return render(request, 'addprescription.html')
    
class Editdoctor(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor_model, pk=pk)
        return render(request, 'editdoctor.html', {'doctor': doctor})
    def post(self, request, pk):
        doctor = get_object_or_404(Doctor_model, pk=pk)
        form = AddDoctor_form(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('viewdoctors')
    
    
class DeleteDoctor(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor_model, pk=pk)
        doctor.delete()
        HttpResponse('''<script> alert("deleted Successfully"); window.location.href='/viewdoctors' </script>''')
        return redirect('viewdoctors')
    
class EditMedicine(View):
    def get(self, request, pk):
        medicine = get_object_or_404(Medicine_model, pk=pk)
        return render(request, 'editmedicine.html', {'medicine': medicine})
    def post(self, request, pk):
        medicine = get_object_or_404(Medicine_model, pk=pk)
        form = AddMedicine_form(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('viewmedicine')
        
class DeleteMedicine(View):
    def get(self, request, pk):
        med = get_object_or_404(Medicine_model, pk=pk)
        med.delete()
        return HttpResponse(''' <script> alert("deleted successfully"); window.location.href='/viewmedicine' </script> ''')
    
class EditPharmacy(View):
    def get(self, request, pk):
        pharmacy = get_object_or_404(Pharmacist_model, pk=pk)
        return render(request, 'editpharmacy.html', {'pharmacy':pharmacy})
    def post(self, request, pk):
        pharmacy = get_object_or_404(Pharmacist_model, pk=pk)
        form = RegisterPharmacist_form(request.POST, instance=pharmacy)
        if form.is_valid():
            form.save()
            return redirect('viewpharmacy') 
        
class DeletePharmacy(View):
    def get(self, request, pk):
        pharm = get_object_or_404(Pharmacist_model, pk=pk)
        pharm.delete()
        return HttpResponse(''' <script> alert("deleted successfully"); window.location.href='/viewpharmacy' </script>''')
    
class EditPost(View):
    def get(self, request):
        return render(request, 'editpost.html')
    
class Login(View):
    def get(self, request):
        return render(request, 'Login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj = Login_model.objects.get(username = username, password = password)
            request.session['userid'] = obj.id
            if obj.type == 'admin':
                return redirect('adminhome')
            elif obj.type == 'doctor':
                return redirect('doctordash')
            elif obj.type == 'serviceprovider':
                return render(request, 'serviceproviderdash.html')
            else:
                return HttpResponse('Invalid credentials')

        except Login_model.DoesNotExist:
            messages.error(request, "invalid username or password")
            return redirect('login')
            
class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')

    
class RegisterPharmacist(View):
    def get(self, request):
        return render(request, 'Registerpharmacist.html')
    def post(self, request):
        c = RegisterPharmacist_form(request.POST)
        if c.is_valid():
            try:
                Pharm = c.save(commit=False)
                Pharm.LOGIN_ID = Login_model.objects.create(username=request.POST['username'], password=request.POST['password'], type='Pharmacist', status='active')
                Pharm.LOGIN_ID.save()
                Pharm.save()
                return HttpResponse('''<script> alert("Pharmacist Registered Successfully"); window.location.href='/registerpharmacist' </script>''')
            except:
                return HttpResponse('''<script> alert("Pharmacist Registration Failed"); window.location.href='/registerpharmacist'</script>''')
    

class ViewBooking(View):
    def get(self, request):
        return render(request, 'viewbooking.html')
    
class ViewDoctors(View):
    def get(self, request):
        c = Doctor_model.objects.all
        return render(request, 'viewdoctors.html', { 's':c })

class ViewMedicines(View):
    def get(self, request):
        c = Medicine_model.objects.all()
        return render(request, 'viewmedicine.html', { 's':c })
    
class ViewMedicineDoc(View):
    def get(self, request):
        return render(request, 'viewmedicinedoc.html')
    
class ViewPharmacy(View):
    def get(self, request):
        c = Pharmacist_model.objects.all()
        return render(request, 'viewpharmacy.html', { 's':c })
    
class ViewPost(View):
    def get(self, request):
        return render(request, 'viewpost.html')
    
class ViewPrescription(View):
    def get(self, request):
        return render(request, 'viewprescription.html')
    
class AdminHome(View):
    def get(self, request):
        return render(request, 'adminDash.html')
    
class View_patient(View):
    def get(self, request):
        c = Patient_model.objects.all()
        return render(request, 'viewpatient.html', {'s':c})

class Doctordash(View):
    def get(self, request):
        return render(request, 'Doctordash.html')