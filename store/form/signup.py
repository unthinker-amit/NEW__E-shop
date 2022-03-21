from django import forms
from store.models import Customer
from django.core import validators
from store.validators import password_check


def isExists(value):
    print(value)
    if Customer.objects.filter(email=value):
        print(value)
        raise forms.ValidationError(
            "Email already registered,Please use another email."
        )


class signup_form(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(
                limit_value=3,
                message="First name should contains 3 to 50 characters only.",
            )
        ],
    )
    last_name = forms.CharField(
        max_length=50,
        validators=[
            validators.MinLengthValidator(
                limit_value=3,
                message="Last name should contains 3 to 50 characters only.",
            )
        ],
    )
    phone = forms.CharField(
        validators=[
            validators.MinLengthValidator(
                limit_value=10, message="Please enter a valid phone number"
            ),
            validators.MaxLengthValidator(limit_value=12, message="Not a valid number"),
        ]
    )
    email = forms.EmailField(
        validators=[
            isExists,
            validators.EmailValidator(message="Enter valid email address."),
        ]
    )
    password = forms.CharField(widget=forms.PasswordInput, validators=[password_check])
