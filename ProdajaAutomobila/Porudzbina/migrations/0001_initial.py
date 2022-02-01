# Generated by Django 3.0.14 on 2022-01-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SalonAutomobila', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Porudzbina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('adresa', models.CharField(max_length=250)),
                ('postanski_broj', models.CharField(max_length=20)),
                ('grad', models.CharField(max_length=100)),
                ('datum_kreiranja', models.DateTimeField(auto_now_add=True)),
                ('datum_azuriranja', models.DateTimeField(auto_now=True)),
                ('placeno', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'porudzbina',
                'verbose_name_plural': 'porudzbine',
                'ordering': ('-datum_kreiranja',),
            },
        ),
        migrations.CreateModel(
            name='StavkaPorudzbine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kolicina', models.PositiveIntegerField(default=1)),
                ('automobil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stavke_porudzbine_a', to='SalonAutomobila.Automobil')),
                ('porudzbina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stavke_porudzbine_p', to='Porudzbina.Porudzbina')),
            ],
        ),
    ]
