from django import forms

from .models import Property, Reservation


class PropertyForm(forms.ModelForm):

	class Meta:
		model = Property

		fields = [
			'description',
			'image_url',
			'tariff',
			'host',
			'city',
		]
		labels = {
			'description': 'description',
			'image_url': 'image_url',
			'tariff': 'Tariff',
			'host': 'Anfitrion',
			'city': 'Ciudad',
		}
		widgets = {
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'image_url': forms.TextInput(attrs={'class':'form-control'}),
			'tariff': forms.TextInput(attrs={'class':'form-control'}),
			'host': forms.Select(attrs={'class':'form-control'}),
			'city': forms.Select(attrs={'class':'form-control'}),
		}


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation

        fields = [
			'guest',
            'property',
    #        'entry',
    #        'exit',
            'total',
		]
    	labels = {
			'guest': 'guest',
            'property': 'property',
    #        'entry': 'entry',
    #        'exit': 'exit',
            'total': 'total',
		}
        widgets = {
            'guest': forms.TextInput(attrs={'class':'form-control'}),
            'property': forms.Select(attrs={'class':'form-control'}),
    #        'entry': forms.DateInput(attrs={'class':'datepicker'}),
    #        'exit': forms.DateInput(attrs={'class':'datepicker'}),
            'total': forms.NumberInput(attrs={'step': 0.25}),
        }