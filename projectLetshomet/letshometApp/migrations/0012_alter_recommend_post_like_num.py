# Generated by Django 3.2.3 on 2021-06-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letshometApp', '0011_alter_recommend_post_like_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend_post',
            name='like_num',
            field=models.IntegerField(default=0),
        ),
    ]