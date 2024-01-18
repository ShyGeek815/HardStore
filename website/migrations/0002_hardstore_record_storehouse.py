# Generated by Django 5.0 on 2024-01-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HardStore_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name_category', models.CharField(max_length=50)),
                ('name_product', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('model_product', models.CharField(max_length=50)),
                ('warranty', models.CharField(max_length=30)),
                ('contry_product', models.CharField(max_length=30)),
                ('price_product', models.FloatField()),
                ('description_product', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Storehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name_storehouse', models.CharField(max_length=50)),
                ('adress_storehouse', models.CharField(max_length=100)),
                ('phone_storehouse', models.CharField(max_length=50)),
            ],
        ),
    ]
