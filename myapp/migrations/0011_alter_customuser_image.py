# Generated by Django 4.1.3 on 2022-12-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/'),
        ),
    ]
