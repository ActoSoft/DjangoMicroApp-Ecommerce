# Generated by Django 3.0.6 on 2020-05-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products/')),
                ('category', models.CharField(choices=[('electronics', 'Electrónicos'), ('cameras', 'Cámaras'), ('computers', 'Computadoras'), ('cellphones', 'Celulares'), ('accesories', 'Accesorios')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]