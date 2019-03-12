# Generated by Django 2.1.2 on 2019-03-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalin', '0005_auto_20181213_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('display_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('owner_name', models.CharField(max_length=255, null=True)),
                ('contact_email', models.CharField(max_length=255, null=True)),
                ('is_bi', models.CharField(max_length=1)),
            ],
        ),
    ]
