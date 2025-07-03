from django import forms
class StudentForm(forms.Form):
    input_class = 'px-2 py-1 w-full border border-gray-300 rounded'

    rollno=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class': input_class}))
    name=forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'class': input_class}))
    course=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': input_class}))
    message=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': input_class}))