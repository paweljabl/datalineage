# Generated by Django 2.1.2 on 2019-03-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0017_relation_load'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation_load',
            name='relation_level',
            field=models.IntegerField(null=True),
        ),
    ]
