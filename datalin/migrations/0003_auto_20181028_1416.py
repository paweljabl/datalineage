# Generated by Django 2.1.2 on 2018-10-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0002_auto_20181028_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='short_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]