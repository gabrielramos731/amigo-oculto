# Generated by Django 5.1.2 on 2024-12-03 20:12

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_participante_grupo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participante',
            name='codigo_match',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
    ]
