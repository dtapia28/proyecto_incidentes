# Generated by Django 3.2.3 on 2021-07-09 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='pais',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='registro.pais'),
            preserve_default=False,
        ),
    ]
