# Generated by Django 4.2.1 on 2023-05-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_blog_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='path',
            field=models.CharField(max_length=500, null=True),
        ),
    ]