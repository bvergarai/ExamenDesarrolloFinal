# Generated by Django 2.1.2 on 2018-12-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascensor', '0004_registrocliente_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordentrabajo',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
