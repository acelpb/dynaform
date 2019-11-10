# Generated by Django 2.2.7 on 2019-11-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynaform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='participative_kitchen',
            field=models.IntegerField(choices=[(0, 'non'), (1, 'secondaire'), (2, 'importante'), (3, 'essentielle')], default=-1),
        ),
        migrations.AddField(
            model_name='preference',
            name='price_markup',
            field=models.IntegerField(choices=[(10, '10%'), (25, '25%'), (50, '50%'), (100, '50%+')], default=-1),
        ),
        migrations.AlterField(
            model_name='preference',
            name='fairtrade',
            field=models.IntegerField(choices=[(0, 'pas'), (1, 'secondaire'), (2, 'présent'), (3, 'essentiel')], default='', verbose_name='équitable'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='local',
            field=models.IntegerField(choices=[(0, 'pas'), (1, 'secondaire'), (2, 'présent'), (3, 'essentiel')], default='', verbose_name='local'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='organic',
            field=models.IntegerField(choices=[(0, 'pas'), (1, 'secondaire'), (2, 'présent'), (3, 'essentiel')], default='', verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='sustainable',
            field=models.IntegerField(choices=[(0, 'pas'), (1, 'secondaire'), (2, 'présent'), (3, 'essentiel')], default='', verbose_name='durable'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='vegetarian',
            field=models.BooleanField(choices=[(True, 'oui'), (False, 'non')], default='', verbose_name='végétarien'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='zero_waste',
            field=models.IntegerField(choices=[(0, 'pas'), (1, 'secondaire'), (2, 'présent'), (3, 'essentiel')], default='', verbose_name='zéro déchet'),
        ),
    ]
