# Generated by Django 3.2 on 2021-05-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Category name'),
        ),
    ]
