
from django import forms
from .models import Signup1

GENDER_CHOICES= [
    ('', 'I am...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'other'),
    ]

College_CHOICES= [
    ('', 'Select College'),
    ('Pravara Rural Engineering College', 'Pravara Rural Engineering College'),
    ('Rural Dental College', 'Rural Dental College'),
    ('Pravara Institute of Medical Sciences', 'Pravara Institute of Medical Sciences'),
    ('Rural Medical College, Loni', 'Rural Medical College, Loni'),
    ('Pravara Rural College of Pharmacy', 'Pravara Rural College of Pharmacy'),
    ('Pravara Rural College Of Architecture,Loni', 'Pravara Rural College Of Architecture,Loni'),
    ('Nursing College, PMT', 'Nursing College, PMT'),
    ('Padmashri Vikhe Patil College of Arts Science and Commerce', 'Padmashri Vikhe Patil College of Arts Science and Commerce'),
    ('Pravara Womens College of Home Science and BCA', 'Pravara Womens College of Home Science and BCA'),
    ('Pravara College Of Physical Education', 'Pravara College Of Physical Education'),
    ('Pravara Rural College of Pharmacy(Diploma)', 'Pravara Rural College of Pharmacy(Diploma)'),
    ('Pravara Rural Education Societys', 'Pravara Rural Education Societys'),
    ('Pravara Rural Education Societys Padmashri Vikhhe Patil College of Arts, Science and Commerce', 'Pravara Rural Education Societys Padmashri Vikhhe Patil College of Arts, Science and Commerce'),
    ('Pravara Rural ITI COLLEGE', 'Pravara Rural ITI COLLEGE'),
    ('Pravara Rural Engg. College, Loni (Mech. Civil and Chemical dept.)', 'Pravara Rural Engg. College, Loni (Mech. Civil and Chemical dept.)'),

    ]
Eduction_CHOICES= [
    ('', 'Select Eduction'),
    ('B.E Mechanical Engineering', 'B.E Mechanical Engineering'),
    ('MCS', 'MCS'),
    ('MCA', 'MCA'),
    ('BCS', 'BCS'),
    ]

class Signup1form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'size':'65'}))
    first_name=forms.CharField(label='Firstname:',max_length=30, widget=forms.TextInput(attrs={'size':'65'}))
    last_name=forms.CharField(label='Lastname.:',max_length=30, widget=forms.TextInput(attrs={'size':'65'}))

    password1 = forms.CharField(label='Password :', widget=forms.PasswordInput(attrs={'size':'65'}))
    password2 = forms.CharField(label='Reenter_P:', widget=forms.PasswordInput(attrs={'size':'65'}))
    
    Birth_date= forms.DateField(widget=forms.SelectDateWidget())
    
    gender= forms.CharField(label='Gender___',required=True,widget=forms.Select(choices=GENDER_CHOICES,attrs={'style': 'width:75px'}))

    college= forms.CharField(label='College___',required=True,widget=forms.Select(choices=College_CHOICES,attrs={'style': 'width:130px'}))

    qualification= forms.CharField(label='Eduction_.:',required=True,widget=forms.Select(choices=Eduction_CHOICES,attrs={'style': 'width:187px'}))
    
    email=forms.CharField(label='Email_____.:',max_length=30, widget=forms.TextInput(attrs={'size':'65'}))

    mobile=forms.CharField(label='Mobile___.:',max_length=30, widget=forms.TextInput(attrs={'size':'65'}))

    city=forms.CharField(label='City_______:',max_length=30, widget=forms.TextInput(attrs={'size':'65'}))

    address = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))


    class Meta:
        model= Signup1
        fields= ["username", "first_name",
                 "last_name",
                  "password1",
                 "password2",
                 "Birth_date",
                 "gender",
                 "college",
                 "qualification",
                 

                 "email", "mobile", 
                 "city","address"
                 ]


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password1= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)


