# Generated by Django 4.0.4 on 2022-07-11 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_estado_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='usuarioDjango',
        ),
    ]
