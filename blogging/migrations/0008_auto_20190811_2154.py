# Generated by Django 2.1.1 on 2019-08-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0007_auto_20190811_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='post', to='blogging.Category'),
        ),
    ]
