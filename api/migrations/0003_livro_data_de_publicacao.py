# Generated by Django 5.1.2 on 2024-11-04 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_livro_autor_remove_livro_vendas'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='data_de_publicacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
