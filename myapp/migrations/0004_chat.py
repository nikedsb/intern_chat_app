# Generated by Django 3.2.15 on 2022-08-29 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_customuser_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('chat_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_from', to=settings.AUTH_USER_MODEL)),
                ('chat_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]