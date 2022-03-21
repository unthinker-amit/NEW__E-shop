from django.core import validators
from django import forms
from store.models import Category


class AddProduct(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[
            validators.MaxLengthValidator(
                limit_value=50,
                message="name should contains 3 to 50 characters only.",
            )
        ],
    )
    price = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    description = forms.CharField(
        max_length=200,
        validators=[
            validators.MaxLengthValidator(
                limit_value=200,
                message="Description should not more than 200 characters.",
            )
        ],
    )
    image = forms.ImageField(required=False, allow_empty_file=True)
