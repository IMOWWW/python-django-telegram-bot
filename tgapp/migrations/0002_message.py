# Generated by Django 4.1.3 on 2022-11-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]