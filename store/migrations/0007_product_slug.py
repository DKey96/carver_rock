# Generated by Django 3.1.3 on 2022-01-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220109_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
