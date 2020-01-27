# Generated by Django 3.0.2 on 2020-01-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta_programar_cita', '0003_auto_20200122_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='dia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='dx',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='estado',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_actualizacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_creacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_hora',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='lugar_residencia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='observaciones',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='primer_apellido',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='psiquiatra',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='segundo_apellido',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='sexo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
    ]