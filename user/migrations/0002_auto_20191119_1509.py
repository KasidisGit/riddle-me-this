# Generated by Django 2.2.5 on 2019-11-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default='guest', max_length=254, null=True),
        ),
    ]
