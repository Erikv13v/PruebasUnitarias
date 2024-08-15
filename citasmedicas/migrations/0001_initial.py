# Generated by Django 4.2.3 on 2023-07-11 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, verbose_name='')),
                ('contraseña', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('costo', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveSmallIntegerField()),
                ('especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasmedicas.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasmedicas.paciente')),
            ],
        ),
    ]
