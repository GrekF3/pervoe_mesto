from django import forms

class ClientForm(forms.Form):
    
    phone_contact = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'quiz-manager__form-input',
        'placeholder': '+ 7 999 123 45 67',
        'data-inputmask': "'mask': '+7 (999) 999-99-99'",
        'pattern': r'\+7(\s+)?\(?\d{3}\)?(\s+)?\d{3}(\s+)?(-)?\d{2}(\s+)?(-)?\d{2}',
        'autocomplete': 'tel',
        'required': 'required'
    }))


class PriceForm(forms.Form):
    from_value = forms.CharField(widget=forms.HiddenInput, initial='Получить прайс')
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'modal__input',
            'placeholder': '+7 999 123 45 67',
            'pattern': r'\+7(\s+)?\(?\d{3}\)?(\s+)?\d{3}(\s+)?(-)?\d{2}(\s+)?(-)?\d{2}',
            'required': 'required',
            'autocomplete': 'tel'
        })
    )
    whatsapp = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'whatsapp'}), required=False)
    sms = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'sms'}), required=False)
    tg = forms.CharField(widget=forms.HiddenInput(attrs={'value': 'tg'}), required=False)

class CalculatorForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'calculator-result__input',
            'placeholder': 'ФИО',
            'required': True,
            'autocomplete': 'name',
        })
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'calculator-result__input input-phone-js',
            'placeholder': '+7 999 123 45 67',
            'pattern': r'\+7(\s+)?\(?\d{3}\)?(\s+)?\d{3}(\s+)?(-)?\d{2}(\s+)?(-)?\d{2}',
            'required': True,
            'autocomplete': 'tel',
        })
    )