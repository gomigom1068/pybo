# Generated by Django 3.2.5 on 2021-07-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]