# Generated by Django 2.2.5 on 2019-10-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entrada_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='enlace',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entrada',
            name='informacion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]