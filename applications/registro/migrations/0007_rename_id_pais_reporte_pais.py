# Generated by Django 3.2.3 on 2021-07-26 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_alter_comuna_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte',
            old_name='id_pais',
            new_name='pais',
        ),
    ]