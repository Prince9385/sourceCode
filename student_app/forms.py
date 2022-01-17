from django import forms
from .models import  StudentInfo
from .models import StudentAcademics



# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model=StudentInfo
#         fields=['Rollno']
#         widgets={
#             'Rollno': forms.TextInput(attrs={'class': 'form-control'})
#         }
class StudentRegistration2(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields=['Rollno','Name','Class','School','Mobile','Address']
        widgets={
            'Rollno':forms.TextInput(attrs={'class':'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Class': forms.TextInput(attrs={'class': 'form-control'}),
            'School': forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),

            
        }

class StudentRegistration1(forms.ModelForm):
    class Meta:
        model=StudentAcademics
        fields=[ 'Maths','Physics','Chemistry','Biology','English']
        widgets={
            'Maths':forms.TextInput(attrs={'class':'form-control'}),
            'Physics':forms.TextInput(attrs={'class':'form-control'}),
            'Chemistry':forms.TextInput(attrs={'class':'form-control'}),
            'Biology':forms.TextInput(attrs={'class':'form-control'}),
            'English':forms.TextInput(attrs={'class':'form-control'}),

        }

    