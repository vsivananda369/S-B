from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = [
            "first_name",
            "last_name",
            "mobile",
            "email",
            "pan_number",
            "aadhaar_number",
            "account_number",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter First Name"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Last Name"
                }
            ),

            "mobile": forms.TextInput(
                attrs={
                    "placeholder": "Enter Mobile Number"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter Email"
                }
            ),

            "pan_number": forms.TextInput(
                attrs={
                    "placeholder": "PAN Number"
                }
            ),

            "aadhaar_number": forms.TextInput(
                attrs={
                    "placeholder": "Aadhaar Number"
                }
            ),

            "account_number": forms.TextInput(
                attrs={
                    "placeholder": "Account Number"
                }
            ),
        }