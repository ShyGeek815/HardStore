# Generated by Django 5.0 on 2023-12-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('familia', models.CharField(max_length=50)),
                ('imya', models.CharField(max_length=50)),
                ('otchestvo', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=60)),
            ],
        ),
    ]