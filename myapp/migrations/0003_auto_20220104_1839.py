# Generated by Django 3.1 on 2022-01-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220102_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talker',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]