# Generated by Django 2.2.4 on 2019-08-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
