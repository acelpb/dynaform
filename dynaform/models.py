from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

CRITERIAS = {
    'organic': _('bio'),
    'sustainable': _('durable'),
    'fairtrade': _('fairtrade'),
    'local': _('local'),
    'zero_waste': _('zéro déchet'),
}

ETHIC_CHOICES = (
    (0, _("pas")),
    (1, _("secondaire")),
    (2, _('présent')),
    (3, _('essentiel')),
)


def validate_ordrered_criterias(value):
    criterias = set(value.split(','))

    error_message = ""
    if criterias - CRITERIAS.keys():
        error_message += _('The following criterias are invalid: ') + ', '.join(criterias - CRITERIAS)
    if CRITERIAS.keys() - criterias:
        error_message += _('The following criterias are missing: ') + ', '.join(CRITERIAS - criterias)

    if error_message:
        raise ValidationError(error_message)


# Create your models here.
class Preference(models.Model):
    BOOL_CHOICES = ((True, 'oui'), (False, 'non'))
    ETHIC_CHOICES = ETHIC_CHOICES

    vegetarian = models.BooleanField(choices=BOOL_CHOICES, default='', verbose_name=('végétarien'))

    participative_kitchen = models.IntegerField(
        choices=(
            (0, "non"),
            (1, "secondaire"),
            (2, "importante"),
            (3, "essentielle"),
        ),
        default=-1,
        blank=False
    )

    organic = models.IntegerField(choices=ETHIC_CHOICES, default='', blank=False, verbose_name=_('bio'))
    sustainable = models.IntegerField(choices=ETHIC_CHOICES, default='', blank=False, verbose_name=_('durable'))
    fairtrade = models.IntegerField(choices=ETHIC_CHOICES, default='', blank=False, verbose_name=_('équitable'))
    local = models.IntegerField(choices=ETHIC_CHOICES, default='', blank=False, verbose_name=_('local'))
    zero_waste = models.IntegerField(choices=ETHIC_CHOICES, default='', blank=False, verbose_name=_('zéro déchet'))

    entity_type = models.TextField(choices=(
        ('social', _('Uniquement des sociétés/associations avec une vocation sociale et / ou sociétale')),
        ('pme', _('Uniquement des pme')),
        ('all', _('Tous type de structure (p.ex.sodexo)')),
    ), default='')

    price_markup = models.IntegerField(
        choices=(
            (10, '10%'),
            (25, '25%'),
            (50, '50%'),
            (100, '50%+'),
        ), default=-1)

