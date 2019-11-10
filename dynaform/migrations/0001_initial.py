# Generated by Django 2.2.7 on 2019-11-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetarian', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='', verbose_name='végétarien')),
                ('organic', models.IntegerField(choices=[(1, 'pas'), (2, 'annexe'), (3, 'présent'), (4, 'essentiel')], default='', verbose_name='bio')),
                ('sustainable', models.IntegerField(choices=[(1, 'pas'), (2, 'annexe'), (3, 'présent'), (4, 'essentiel')], default='', verbose_name='durable')),
                ('fairtrade', models.IntegerField(choices=[(1, 'pas'), (2, 'annexe'), (3, 'présent'), (4, 'essentiel')], default='', verbose_name='équitable')),
                ('local', models.IntegerField(choices=[(1, 'pas'), (2, 'annexe'), (3, 'présent'), (4, 'essentiel')], default='', verbose_name='local')),
                ('zero_waste', models.IntegerField(choices=[(1, 'pas'), (2, 'annexe'), (3, 'présent'), (4, 'essentiel')], default='', verbose_name='zéro déchet')),
                ('entity_type', models.TextField(choices=[('social', 'Uniquement des sociétés/associations avec une vocation sociale et / ou sociétale'), ('pme', 'Uniquement des pme'), ('all', 'Tous type de structure (p.ex.sodexo)')], default='')),
            ],
        ),
    ]