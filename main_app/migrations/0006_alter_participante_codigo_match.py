# Generated by Django 5.1.3 on 2024-12-10 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_grupo_admin_alter_participante_codigo_match_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='codigo_match',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.participante'),
        ),
    ]
