# Generated by Django 2.1.2 on 2019-03-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0018_auto_20190313_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Full_Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=255)),
                ('a_display_name', models.CharField(max_length=100, null=True)),
                ('a_description', models.CharField(max_length=500, null=True)),
                ('a_entity', models.CharField(max_length=100, null=True)),
                ('a_technology', models.CharField(max_length=100, null=True)),
                ('relation_type', models.CharField(max_length=30)),
                ('relation_level', models.IntegerField(null=True)),
                ('b_name', models.CharField(max_length=255)),
                ('b_display_name', models.CharField(max_length=100, null=True)),
                ('b_description', models.CharField(max_length=500, null=True)),
                ('b_entity', models.CharField(max_length=100, null=True)),
                ('b_technology', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]