from django import forms


input_class = 'px-2 py-1 bg-white w-full border border-gray-300 rounded'
class StudentForm(forms.Form):
    rollno=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class': input_class}))
    name=forms.CharField(max_length=20, required=True,widget=forms.TextInput(attrs={'class': input_class}))
    course=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class': input_class}))
    message=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': input_class}))


class RegisterForm(forms.Form):
    username=forms.CharField(max_length=12,widget=forms.TextInput(attrs={'class': input_class}))
    password=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class': input_class}))
    confirmpassword=forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class': input_class}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmpassword")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirmpassword', "Password does not match with confirm password")
        return cleaned_data