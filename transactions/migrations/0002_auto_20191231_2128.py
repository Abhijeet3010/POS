# Generated by Django 3.0.1 on 2019-12-31 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='customer_phoneno',
            field=models.IntegerField(),
        ),
    ]