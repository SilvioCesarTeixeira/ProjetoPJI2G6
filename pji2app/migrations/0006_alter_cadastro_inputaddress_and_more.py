# Generated by Django 4.0.4 on 2022-05-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pji2app', '0005_alter_cadastro_inputaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='inputAddress',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='inputAddress2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
