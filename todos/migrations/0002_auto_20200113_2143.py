# Generated by Django 3.0.2 on 2020-01-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]