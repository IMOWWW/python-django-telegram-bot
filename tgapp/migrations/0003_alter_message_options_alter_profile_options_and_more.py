# Generated by Django 4.1.3 on 2022-11-28 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgapp', '0002_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.CreateModel(
            name='MessageMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(verbose_name='Полученное сообщение')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tgapp.profile', verbose_name='Пользователь')),
            ],
        ),
    ]
