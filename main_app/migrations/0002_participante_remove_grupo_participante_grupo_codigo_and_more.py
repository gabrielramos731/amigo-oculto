# Generated by Django 5.1.2 on 2024-11-28 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='participante',
        ),
        migrations.AddField(
            model_name='grupo',
            name='codigo',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='participantes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.participante'),
        ),
    ]