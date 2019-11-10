from django.views.generic import CreateView

from dynaform.forms import PreferenceForm
from .models import Preference


class PreferenceCreateView(CreateView):
    model = Preference
    form_class = PreferenceForm

    def get_success_url(self):
        return '/thanks'

    def form_invalid(self, form):
        print('toto')
        print(form.data)
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print('tata')
        print(form.data)
        return super().form_valid(form)
