# Generated by Django 4.0.4 on 2022-06-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_pub_data_talk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default/light.png', upload_to='media/%Y/%m/%d/', verbose_name='アイコン画像'),
        ),
    ]
