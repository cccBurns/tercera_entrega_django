# Generated by Django 4.2.6 on 2023-11-01 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_productos_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
    ]
