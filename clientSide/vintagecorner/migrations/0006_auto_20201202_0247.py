# Generated by Django 3.1.3 on 2020-12-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintagecorner', '0005_auto_20201202_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensmenu',
            name='ordem',
            field=models.IntegerField(choices=[(2, 'Carne'), (3, 'Vegetariana'), (6, 'Bolos'), (50, 'Agua'), (54, 'Cafe'), (59, 'Cerveja'), (63, 'Whisky')], default=0),
        ),
    ]
