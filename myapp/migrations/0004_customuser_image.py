# Generated by Django 4.2.2 on 2023-08-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='seikin.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
