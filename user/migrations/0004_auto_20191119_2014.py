# Generated by Django 2.2.5 on 2019-11-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20191119_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='guest', max_length=254, unique=True),
        ),
    ]
