# Generated by Django 4.0.4 on 2022-05-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pji2app', '0003_alter_cadastro_inputemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='inputCEP',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputCel',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputTel',
            field=models.CharField(max_length=10),
        ),
    ]
