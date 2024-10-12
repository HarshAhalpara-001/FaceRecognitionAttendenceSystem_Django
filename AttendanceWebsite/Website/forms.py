from django import forms
from .models import StudentImage

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentImage
        fields = ['class_name', 'division', 'roll_no', 'name']
        labels = {
            'class_name': 'Class',
            'division': 'Division',
            'roll_no': 'Roll Number',
            'name': 'Name'
        }

        widgets = {
            'class_name': forms.Select(choices=[
                ('1', '1st'),
                ('2', '2nd'),
                ('3', '3rd'),
                ('4', '4th'),
                ('5', '5th'),
                # Add more classes as needed
            ]),
            'division': forms.Select(choices=[
                ('A', 'A'),
                ('B', 'B'),
                ('C', 'C'),
                # Add more divisions as needed
            ]),
        }
