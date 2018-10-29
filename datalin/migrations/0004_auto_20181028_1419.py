# Generated by Django 2.1.2 on 2018-10-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0003_auto_20181028_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='contact_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='owner_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='short_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='relation_type',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='short_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
