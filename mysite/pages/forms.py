from django import forms


class ContactSellerForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(label='Your email')
    phone = forms.CharField(max_length=15, required=False, label='Phone (optional)')
    product = forms.ChoiceField(label='Product')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    def __init__(self, *args, product_choices=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].choices = product_choices
