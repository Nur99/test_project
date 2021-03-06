# Generated by Django 2.2.6 on 2020-03-31 13:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='Ключ')),
            ],
            options={
                'verbose_name': 'Ключ',
                'verbose_name_plural': 'Ключи',
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('key', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Key')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
    ]
