# Generated by Django 3.1.3 on 2020-12-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintagecorner', '0004_auto_20201202_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensmenu',
            name='ordem',
            field=models.DecimalField(choices=[(1.21, 'Carne'), (1.4, 'Vegetariana'), (1.6, 'Bolos'), (3.0, 'Agua'), (3.1, 'Cafe'), (3.3, 'Cerveja'), (3.5, 'Whisky')], decimal_places=2, max_digits=4),
        ),
    ]
