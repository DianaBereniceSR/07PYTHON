# Generated by Django 2.1.2 on 2018-12-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='critica',
            name='calificacion',
            field=models.IntegerField(null=True),
        ),
    ]
