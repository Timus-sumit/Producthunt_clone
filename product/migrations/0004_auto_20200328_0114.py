# Generated by Django 3.0.4 on 2020-03-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200328_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=400),
        ),
    ]