from django import forms

class BankConnectForm(forms.Form):
    token = forms.CharField(
        label="Monobank token",
        widget=forms.PasswordInput,  
        max_length=255
    )