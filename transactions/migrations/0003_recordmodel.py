# Generated by Django 3.0.1 on 2020-01-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20191231_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='recordmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.IntegerField()),
                ('items_ids', models.TextField()),
                ('items_quantity', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
