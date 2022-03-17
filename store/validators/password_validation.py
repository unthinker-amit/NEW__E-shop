from django import forms


def password_check(passwd):

    SpecialSym = ["$", "@", "#", "%"]

    if len(passwd) < 6:
        raise forms.ValidationError("length should be at least 6")

    if len(passwd) > 20:
        raise forms.ValidationError("length should be not be greater than 20")

    if not any(char.isdigit() for char in passwd):
        raise forms.ValidationError("Password should have at least one numeral")

    if not any(char.isupper() for char in passwd):
        raise forms.ValidationError(
            "Password should have at least one uppercase letter"
        )

    if not any(char.islower() for char in passwd):
        raise forms.ValidationError(
            "Password should have at least one lowercase letter"
        )

    if not any(char in SpecialSym for char in passwd):
        raise forms.ValidationError(
            "Password should have at least one of the symbols $@#"
        )
