from django import forms
from .models import User, Admin, Cat, MedicalRecord

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'address', 'email', 'password']

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'username', 'password']

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'type', 'details']
    
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['catname', 'veterinarian', 'diagnosis', 'treatment_plan',
                  'medication_prescribed', 'next_appointment', 'notes']
