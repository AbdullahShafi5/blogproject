# Generated by Django 3.2 on 2021-05-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
