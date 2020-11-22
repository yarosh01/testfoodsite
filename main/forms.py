from django import forms

# pomenyat delicion
class ContactForm(forms.Form):

    from_email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Phone', required=True)
    chill_time = forms.CharField(label='Дата', required=True)
    delicion = forms.CharField(label='Пожелания', required=True)


