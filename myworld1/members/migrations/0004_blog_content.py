# Generated by Django 4.2.1 on 2023-05-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default=None, max_length=20000),
            preserve_default=False,
        ),
    ]
