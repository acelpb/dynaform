from django.views.generic import CreateView

from dynaform.forms import PreferenceForm
from .models import Preference


class PreferenceCreateView(CreateView):
    model = Preference
    form_class = PreferenceForm

    def get_success_url(self):
        return '/thanks'
