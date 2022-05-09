from tkinter import Widget
from xml.dom.minidom import Document
from django import forms
from .models import Resume
GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICES=[
    ('Delhi','Delhi'),
    ('pune','pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Patna','Patna'),
    ('Bangalore','Bangalore')
]

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICES,widget=forms.
    CheckboxSelectMultiple)                                   
                                       
    class Meta:
        model=Resume
        fields=['name','dob','gender','locality','city','pin',
        'state','mobile','email','job_city','profile_image','my_file']
        
        labels={'name':'FullName','dob':'Date Of Birth','pin':'Pin Code',
        'mobile':'Mobile No.','email':'Email ID','profile_image':'Profile_Image','my_file':'Document'}
        Widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
            }