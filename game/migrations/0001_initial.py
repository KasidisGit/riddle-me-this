# Generated by Django 2.2.5 on 2019-12-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EasyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/easy')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='HardQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/hard')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='MediumQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/medium')),
                ('answer', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=3)),
            ],
        ),
    ]
