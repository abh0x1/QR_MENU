from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=100,
        label="Restaurant Name",
        widget=forms.TextInput(attrs={
            'class': 'bg-white text-black px-2 py-1 rounded border',
            'placeholder':'Enter Restaurat name'
        })
    )
    url = forms.URLField(
        max_length=200,
        label="Menu URL",
        widget=forms.URLInput(attrs={
            'class': 'bg-white text-black px-2 py-1 rounded border',
            'placeholder':'Enter the URL of your online menu'
        })
    )
