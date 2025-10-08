from django import forms
from .models import Color, Auto


class AutoForm(forms.Form):
    TYPE_CHOICES = [('', '-- choose a type --'), ] + [(t.type, t.type) for t in Auto.objects.all()]
    COLOR_CHOICES = [(c.color, c.color) for c in Color.objects.all()]
    COLOR_CHOICES.insert(0, ('', '-- choose a vehicle type first --'))

    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'onchange': 'get_vehicle_color();'}))
    color = forms.ChoiceField(choices=COLOR_CHOICES)
