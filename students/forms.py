from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator

def course_validaator(course):
    if course not in ["python", "java", "mysql"]:
        raise forms.ValidationError("Course must be pthon, java or mysql")
    else:
        return course
    
def upperCaseValidator(name):
    if not name.isupper():
        raise forms.ValidationError("Name must be upper case")
    else:
        return name

input_class = 'px-2 py-1 bg-white w-full border border-gray-300 rounded'
class AddStudentForm(forms.Form):
    name=forms.CharField(validators=[MinLengthValidator(1),MaxLengthValidator(20), upperCaseValidator],widget=forms.TextInput(attrs={'class': input_class}))
    rollno=forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],widget=forms.NumberInput(attrs={'class': input_class}))
    course=forms.CharField(validators=[course_validaator],widget=forms.TextInput(attrs={'class': input_class}))
    # email=forms.CharField(validators=[RegexValidator(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')],widget=forms.TextInput(attrs={'class': input_class}))
    fees=forms.IntegerField(validators=[MinValueValidator(100),MaxValueValidator(100000)],widget=forms.NumberInput(attrs={'class': input_class}))

    def clean_fee(self):
        d=super().clean()
        if d['course']=="python" and d['fee']!=4000:
            raise forms.ValidationError("fee must be 4000")
        elif d['course']=="java" and d['fee']!=2000:
            raise forms.ValidationError("fee must be 2000")
        elif d['course']=="mysql" and d['fee']!=0:
            raise forms.ValidationError("fee must be 0")
        return d

