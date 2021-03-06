# Generated by Django 3.0.2 on 2020-01-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falta_programar_cita', '0005_auto_20200123_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='dx',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_actualizacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='fecha_hora',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='lugar_residencia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='nombre',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='observaciones',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='primer_apellido',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='psiquiatra',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='segundo_apellido',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='sexo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='faltaprogramarcita',
            name='telefono',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
