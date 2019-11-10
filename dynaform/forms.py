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
                       'La participation des Dynamobiliens à la cuisine (épluchage, aide à la préparation) est-elle importante?'
                       '</label>')),
                Div(InlineRadios('participative_kitchen'), css_class='form-inline'),
                css_class='form-group',
            ),
            Div(
                HTML(_('<label>'
                       'De quelle manière les critères suivants font-ils partie de la philosophie de Dynamobile?'
                       '</label>')),
                Div(InlineRadios('organic'), css_class='form-inline'),
                Div(InlineRadios('sustainable'), css_class='form-inline'),
                Div(InlineRadios('fairtrade'), css_class='form-inline'),
                Div(InlineRadios('local'), css_class='form-inline'),
                Div(InlineRadios('zero_waste'), css_class='form-inline'),
                css_class='form-group',
            ),
            'entity_type',
            Div(
                HTML(_('<label>'
                       'Les chois proposés si-dessus se répercute généralement financièrement; '
                       'à cahier de charge égal, quel supplément seriez vous prêt à supporter pour faire en sorte que '
                       'votre préférence soit respectée?'
                       '</label>')),
                Div(InlineRadios('price_markup'), css_class='form-inline'),
                css_class='form-group',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )

        )

    class Meta:
        model = Preference
        fields = '__all__'
        widgets = {
            'vegetarian': forms.RadioSelect(attrs={'autofocus': True}),
            'entity_type': forms.RadioSelect,
            "criteria_order": MyCustomWidget,
            **{criteria: forms.RadioSelect for criteria in CRITERIAS},
        }
        labels = {
            'vegetarian': _('Dynamobile doit-il continuer à être végétarien ?'),
            'entity_type': _('Avec quel type de structure acceptez vous de travailler ?'),
            "criteria_order": _('Veuillez mettre dans l’ordre les critères suivants avec le plus important en haut et le moins important en bas.'),
            "participative_kitchen": "",
            "price_markup": "",
        }

