# Generated by Django 2.2.5 on 2019-10-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191001_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(upload_to='media/archivo/'),
        ),
    ]
