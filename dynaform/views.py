from django.db.models import Count
from django.views.generic import CreateView
from django.views.generic import TemplateView
from plotly.offline.offline import get_plotlyjs

from .forms import PreferenceForm
from .graphs import piechart, barchart, horizontal_barchart
from .models import Preference


class PreferenceCreateView(CreateView):
    model = Preference
    form_class = PreferenceForm

    def get_success_url(self):
        return '/thanks'


class Results(TemplateView):
    template_name = "dynaform/results.html"

    def get_context_data(self, **context):
        vegetarian_options = {
            k: v for k, v in
            Preference.objects.
                values('vegetarian').annotate(Count('vegetarian')).
                values_list('vegetarian', 'vegetarian__count')
        }

        context['vegetarian'] = piechart(
            data=[vegetarian_options.get(k, 0) for k, _ in Preference.BOOL_CHOICES],
            labels=[v for _, v in Preference.BOOL_CHOICES],
        )
        participative_kitchen = {
            k: v for k, v in
            Preference.objects.values('participative_kitchen')
                .annotate(Count('participative_kitchen'))
                .values_list('participative_kitchen', 'participative_kitchen__count')
        }
        context['participative_kitchen'] = barchart(
            data=[participative_kitchen.get(k, 0) for k, _ in Preference.ETHIC_CHOICES_F],
            labels=[v for _, v in Preference.ETHIC_CHOICES_F],
        )

        values = dict()
        values_order = dict()
        for value in ['organic', 'sustainable', 'fairtrade', "local", 'zero_waste']:
            toto = {
                k: v for k, v in
                Preference.objects.values(value)
                    .annotate(Count(value))
                    .values_list(value, value + '__count')
            }
            values[value] = toto

            values_order[value] = sum(
                val * count for val, count in values[value].items()
            )

        ordered_values = sorted(values, key=values_order.get)

        context['values'] = horizontal_barchart(
            data=[
                (str(v), [values[val].get(k, 0) for val in ordered_values])
                for k, v in Preference.ETHIC_CHOICES
            ],
            labels=[str(v) for v in ordered_values],
        )

        entity_type = {
            k: v for k, v in
            Preference.objects.values('entity_type')
                .annotate(Count('entity_type'))
                .values_list('entity_type', 'entity_type__count')
        }

        context['entity_type_label'] = PreferenceForm.Meta.labels['entity_type']
        context['entity_type'] = barchart(
            data=[entity_type.get(k, 0) for k, _ in Preference.ENTITY_CHOICES],
            labels=[str(v) for _, v in Preference.ENTITY_CHOICES],
        )

        price_markup = {
            k: v for k, v in
            Preference.objects.values('price_markup')
                .annotate(Count('price_markup'))
                .values_list('price_markup', 'price_markup__count')
        }

        context['price_markup'] = barchart(
            data=[price_markup.get(k, 0) for k, _ in Preference.INCREASE_CHOICES],
            labels=[str(v) for _, v in Preference.INCREASE_CHOICES],
        )

        context['plotlyjs'] = get_plotlyjs()
        return context
