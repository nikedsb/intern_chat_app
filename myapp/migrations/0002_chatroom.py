# Generated by Django 3.1.1 on 2020-10-11 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=140)),
                ('time', models.DateTimeField(null=True)),
                ('talkfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talkfrom', to=settings.AUTH_USER_MODEL)),
                ('talkto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talkto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
