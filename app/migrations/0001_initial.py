# Generated by Django 4.0.4 on 2022-05-03 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plu_codigo', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=40)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
        ),
    ]
