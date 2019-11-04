# Generated by Django 2.2.5 on 2019-10-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='articles.Hashtag'),
        ),
    ]
