# Generated by Django 3.2.3 on 2021-06-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letshometApp', '0008_auto_20210615_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend_post',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
