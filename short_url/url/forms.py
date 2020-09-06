from django import forms


class CreateNewURL(forms.Form):
    original_url = forms.URLField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Long URL",
                "class": "form-control"
            }),
        label=False
    )
