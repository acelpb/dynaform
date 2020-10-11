from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, ButtonHolder, Div, Layout, Submit
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Message


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "image",
            "message",
            "copyright_holder",
            ButtonHolder(Submit("submit", "Submit", css_class="button white")),
        )

    class Meta:
        model = Message
        fields = ("image", "message", "copyright_holder")
        widgets = {
            "copyright_holder": forms.TextInput,
        }
