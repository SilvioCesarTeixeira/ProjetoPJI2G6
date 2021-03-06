# Generated by Django 4.0.4 on 2022-05-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pji2app', '0006_alter_cadastro_inputaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='inputCNPJ',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputAddress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputCEP',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputCel',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputEmail',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputEmpresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputTel',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
