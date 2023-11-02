from django import forms

class ExpenseUploadForm(forms.Form):
    receipt_image = forms.ImageField(
        label='Upload a receipt or take a photo',
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*', 'capture': 'camera'})
    )
