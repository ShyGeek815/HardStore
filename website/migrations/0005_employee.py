# Generated by Django 5.0 on 2024-01-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_record_position_record_date_of_birth_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('familia', models.CharField(max_length=50)),
                ('imya', models.CharField(max_length=50)),
                ('otchestvo', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=300)),
                ('email', models.CharField(default='@mail', max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('male_choice', models.CharField(max_length=50)),
                ('date_of_birth', models.CharField(default='00.00.2000', max_length=10)),
                ('position', models.CharField(max_length=300)),
            ],
        ),
    ]
