from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Div, HTML
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Preference, CRITERIAS


class MyCustomWidget(forms.widgets.ChoiceWidget):
    template_name = 'dynaform/order.html'
    option_template_name = 'dynaform/list_element.html'
    pass


class PreferenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('vegetarian'),
            Div(
                HTML(_('<label>'
                       'De quel manière les critères suivants font-ils partient de la philosophie de dynamobile?'
                       '</label>')),
                Div(InlineRadios('organic'), css_class='form-inline'),
                Div(InlineRadios('sustainable'), css_class='form-inline'),
                Div(InlineRadios('fairtrade'), css_class='form-inline'),
                Div(InlineRadios('local'), css_class='form-inline'),
                Div(InlineRadios('zero_waste'), css_class='form-inline'),
                css_class='form-group',
            ),
            'entity_type',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )

        )

    class Meta:
        model = Preference
        fields = '__all__'
        widgets = {
            'vegetarian': forms.RadioSelect(
                choices=(
                    (True, _('oui')),
                    (False, _('non')),
                )
            ),
            'entity_type': forms.RadioSelect,
            "criteria_order": MyCustomWidget,
            **{criteria: forms.RadioSelect for criteria in CRITERIAS},
        }
        labels = {
            'vegetarian': _('Dynamobile doit-il continuer à être végétarien ?'),
            'entity_type': _('Avec quel type de structure acceptez vous de travailler ?'),
            "criteria_order": _('Veuillez mettre dans l’ordre les critères suivants avec le plus important en haut et le moins important en bas.'),
        }
